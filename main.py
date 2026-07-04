import uvicorn

import logging
logging.basicConfig(
    level=logging.INFO, # Set the lowest severity level to capture
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),   # Save logs to a file
        logging.StreamHandler()          # Print logs to the console
    ]
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Run the FastAPI application using uvicorn."""
    logger.info("Starting the FastAPI application...")
    uvicorn.run("src.api:webapp", host="127.0.0.1", port=8000, reload=False, reload_excludes=["*.log", "./logs/*"])

if __name__ == "__main__":
    main()
