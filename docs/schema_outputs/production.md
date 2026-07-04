## Table: production.billofmaterials

**Description:** Items required to make bicycles and bicycle subassemblies. It identifies the heirarchical relationship between a parent product and its components.

| Column | Type | Description |
|--------|------|-------------|
| billofmaterialsid | integer | Primary key for BillOfMaterials records. |
| productassemblyid | integer | Parent product identification number. Foreign key to Product.ProductID. |
| componentid | integer | Component identification number. Foreign key to Product.ProductID. |
| startdate | timestamp | Date the component started being used in the assembly item. |
| enddate | timestamp | Date the component stopped being used in the assembly item. |
| unitmeasurecode | character(3) | Standard code identifying the unit of measure for the quantity. |
| bomlevel | smallint | Indicates the depth the component is from its parent (AssemblyID). |
| perassemblyqty | numeric(8,2) | Quantity of the component needed to create the assembly. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_BillOfMaterials_BOMLevel" |  |
| CONSTRAINT | "CK_BillOfMaterials_EndDate" |  |
| CONSTRAINT | "CK_BillOfMaterials_PerAssemblyQty" |  |
| CONSTRAINT | "CK_BillOfMaterials_ProductAssemblyID" |  |


## Table: production.culture

**Description:** Lookup table containing the languages in which some AdventureWorks data is stored.

| Column | Type | Description |
|--------|------|-------------|
| cultureid | character(6) | Primary key for Culture records. |
| name | public."Name" | Culture description. |
| modifieddate | timestamp |  |


## Table: production.document

**Description:** Product maintenance documents.

| Column | Type | Description |
|--------|------|-------------|
| title | character | Title of the document. |
| owner | integer | Employee who controls the document.  Foreign key to Employee.BusinessEntityID |
| folderflag | public."Flag" | 0 = This is a folder, 1 = This is a document. |
| filename | character | File name of the document |
| fileextension | character | File extension indicating the document type. For example, .doc or .txt. |
| revision | character(5) | Revision number of the document. |
| changenumber | integer | Engineering change approval number. |
| status | smallint | 1 = Pending approval, 2 = Approved, 3 = Obsolete |
| documentsummary | text | Document abstract. |
| document | bytea | Complete document. |
| rowguid | uuid | ROWGUIDCOL number uniquely identifying the record. Required for FileStream. |
| modifieddate | timestamp |  |
| documentnode | character | Primary key for Document records. |
| CONSTRAINT | "CK_Document_Status" |  |


## Table: production.illustration

**Description:** Bicycle assembly diagrams.

| Column | Type | Description |
|--------|------|-------------|
| illustrationid | integer | Primary key for Illustration records. |
| diagram | xml | Illustrations used in manufacturing instructions. Stored as XML. |
| modifieddate | timestamp |  |


## Table: production.location

**Description:** Product inventory and manufacturing locations.

| Column | Type | Description |
|--------|------|-------------|
| locationid | integer | Primary key for Location records. |
| name | public."Name" | Location description. |
| costrate | numeric | Standard hourly cost of the manufacturing location. |
| availability | numeric(8,2) | Work capacity (in hours) of the manufacturing location. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_Location_Availability" |  |
| CONSTRAINT | "CK_Location_CostRate" |  |


## Table: production.product

**Description:** Products sold or used in the manfacturing of sold products.

| Column | Type | Description |
|--------|------|-------------|
| productid | integer | Primary key for Product records. |
| name | public."Name" | Name of the product. |
| productnumber | character | Unique product identification number. |
| makeflag | public."Flag" | 0 = Product is purchased, 1 = Product is manufactured in-house. |
| finishedgoodsflag | public."Flag" | 0 = Product is not a salable item. 1 = Product is salable. |
| color | character | Product color. |
| safetystocklevel | smallint | Minimum inventory quantity. |
| reorderpoint | smallint | Inventory level that triggers a purchase order or work order. |
| standardcost | numeric | Standard cost of the product. |
| listprice | numeric | Selling price. |
| size | character | Product size. |
| sizeunitmeasurecode | character(3) | Unit of measure for Size column. |
| weightunitmeasurecode | character(3) | Unit of measure for Weight column. |
| weight | numeric(8,2) | Product weight. |
| daystomanufacture | integer | Number of days required to manufacture the product. |
| productline | character(2) | R = Road, M = Mountain, T = Touring, S = Standard |
| class | character(2) | H = High, M = Medium, L = Low |
| style | character(2) | W = Womens, M = Mens, U = Universal |
| productsubcategoryid | integer | Product is a member of this product subcategory. Foreign key to ProductSubCategory.ProductSubCategoryID. |
| productmodelid | integer | Product is a member of this product model. Foreign key to ProductModel.ProductModelID. |
| sellstartdate | timestamp | Date the product was available for sale. |
| sellenddate | timestamp | Date the product was no longer available for sale. |
| discontinueddate | timestamp | Date the product was discontinued. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_Product_Class" |  |
| CONSTRAINT | "CK_Product_DaysToManufacture" |  |
| CONSTRAINT | "CK_Product_ListPrice" |  |
| CONSTRAINT | "CK_Product_ProductLine" |  |
| CONSTRAINT | "CK_Product_ReorderPoint" |  |
| CONSTRAINT | "CK_Product_SafetyStockLevel" |  |
| CONSTRAINT | "CK_Product_SellEndDate" |  |
| CONSTRAINT | "CK_Product_StandardCost" |  |
| CONSTRAINT | "CK_Product_Style" |  |
| CONSTRAINT | "CK_Product_Weight" |  |


## Table: production.productcategory

**Description:** High-level product categorization.

| Column | Type | Description |
|--------|------|-------------|
| productcategoryid | integer | Primary key for ProductCategory records. |
| name | public."Name" | Category description. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: production.productcosthistory

**Description:** Changes in the cost of a product over time.

| Column | Type | Description |
|--------|------|-------------|
| productid | integer | Product identification number. Foreign key to Product.ProductID |
| startdate | timestamp | Product cost start date. |
| enddate | timestamp | Product cost end date. |
| standardcost | numeric | Standard cost of the product. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_ProductCostHistory_EndDate" |  |
| CONSTRAINT | "CK_ProductCostHistory_StandardCost" |  |


## Table: production.productdescription

**Description:** Product descriptions in several languages.

| Column | Type | Description |
|--------|------|-------------|
| productdescriptionid | integer | Primary key for ProductDescription records. |
| description | character | Description of the product. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: production.productdocument

**Description:** Cross-reference table mapping products to related product documents.

| Column | Type | Description |
|--------|------|-------------|
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| modifieddate | timestamp |  |
| documentnode | character | Document identification number. Foreign key to Document.DocumentNode. |


## Table: production.productinventory

**Description:** Product inventory information.

| Column | Type | Description |
|--------|------|-------------|
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| locationid | smallint | Inventory location identification number. Foreign key to Location.LocationID. |
| shelf | character | Storage compartment within an inventory location. |
| bin | smallint | Storage container on a shelf in an inventory location. |
| quantity | smallint | Quantity of products in the inventory location. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_ProductInventory_Bin" |  |


## Table: production.productlistpricehistory

**Description:** Changes in the list price of a product over time.

| Column | Type | Description |
|--------|------|-------------|
| productid | integer | Product identification number. Foreign key to Product.ProductID |
| startdate | timestamp | List price start date. |
| enddate | timestamp | List price end date |
| listprice | numeric | Product list price. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_ProductListPriceHistory_EndDate" |  |
| CONSTRAINT | "CK_ProductListPriceHistory_ListPrice" |  |


## Table: production.productmodel

**Description:** Product model classification.

| Column | Type | Description |
|--------|------|-------------|
| productmodelid | integer | Primary key for ProductModel records. |
| name | public."Name" | Product model description. |
| catalogdescription | xml | Detailed product catalog information in xml format. |
| instructions | xml | Manufacturing instructions in xml format. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: production.productmodelillustration

**Description:** Cross-reference table mapping product models and illustrations.

| Column | Type | Description |
|--------|------|-------------|
| productmodelid | integer | Primary key. Foreign key to ProductModel.ProductModelID. |
| illustrationid | integer | Primary key. Foreign key to Illustration.IllustrationID. |
| modifieddate | timestamp |  |


## Table: production.productmodelproductdescriptionculture

**Description:** Cross-reference table mapping product descriptions and the language the description is written in.

| Column | Type | Description |
|--------|------|-------------|
| productmodelid | integer | Primary key. Foreign key to ProductModel.ProductModelID. |
| productdescriptionid | integer | Primary key. Foreign key to ProductDescription.ProductDescriptionID. |
| cultureid | character(6) | Culture identification number. Foreign key to Culture.CultureID. |
| modifieddate | timestamp |  |


## Table: production.productphoto

**Description:** Product images.

| Column | Type | Description |
|--------|------|-------------|
| productphotoid | integer | Primary key for ProductPhoto records. |
| thumbnailphoto | bytea | Small image of the product. |
| thumbnailphotofilename | character | Small image file name. |
| largephoto | bytea | Large image of the product. |
| largephotofilename | character | Large image file name. |
| modifieddate | timestamp |  |


## Table: production.productproductphoto

**Description:** Cross-reference table mapping products and product photos.

| Column | Type | Description |
|--------|------|-------------|
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| productphotoid | integer | Product photo identification number. Foreign key to ProductPhoto.ProductPhotoID. |
| "primary" | public."Flag" | 0 = Photo is not the principal image. 1 = Photo is the principal image. |
| modifieddate | timestamp |  |


## Table: production.productreview

**Description:** Customer reviews of products they have purchased.

| Column | Type | Description |
|--------|------|-------------|
| productreviewid | integer | Primary key for ProductReview records. |
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| reviewername | public."Name" | Name of the reviewer. |
| reviewdate | timestamp | Date review was submitted. |
| emailaddress | character |  |
| rating | integer | Product rating given by the reviewer. Scale is 1 to 5 with 5 as the highest rating. |
| comments | character |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_ProductReview_Rating" |  |


## Table: production.productsubcategory

**Description:** Product subcategories. See ProductCategory table.

| Column | Type | Description |
|--------|------|-------------|
| productsubcategoryid | integer | Primary key for ProductSubcategory records. |
| productcategoryid | integer | Product category identification number. Foreign key to ProductCategory.ProductCategoryID. |
| name | public."Name" | Subcategory description. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: production.scrapreason

**Description:** Manufacturing failure reasons lookup table.

| Column | Type | Description |
|--------|------|-------------|
| scrapreasonid | integer | Primary key for ScrapReason records. |
| name | public."Name" | Failure description. |
| modifieddate | timestamp |  |


## Table: production.transactionhistory

**Description:** Record of each purchase order, sales order, or work order transaction year to date.

| Column | Type | Description |
|--------|------|-------------|
| transactionid | integer | Primary key for TransactionHistory records. |
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| referenceorderid | integer | Purchase order, sales order, or work order identification number. |
| referenceorderlineid | integer | Line number associated with the purchase order, sales order, or work order. |
| transactiondate | timestamp | Date and time of the transaction. |
| transactiontype | character(1) | W = WorkOrder, S = SalesOrder, P = PurchaseOrder |
| quantity | integer | Product quantity. |
| actualcost | numeric | Product cost. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_TransactionHistory_TransactionType" |  |


## Table: production.transactionhistoryarchive

**Description:** Transactions for previous years.

| Column | Type | Description |
|--------|------|-------------|
| transactionid | integer | Primary key for TransactionHistoryArchive records. |
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| referenceorderid | integer | Purchase order, sales order, or work order identification number. |
| referenceorderlineid | integer | Line number associated with the purchase order, sales order, or work order. |
| transactiondate | timestamp | Date and time of the transaction. |
| transactiontype | character(1) | W = Work Order, S = Sales Order, P = Purchase Order |
| quantity | integer | Product quantity. |
| actualcost | numeric | Product cost. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_TransactionHistoryArchive_TransactionType" |  |


## Table: production.unitmeasure

**Description:** Unit of measure lookup table.

| Column | Type | Description |
|--------|------|-------------|
| unitmeasurecode | character(3) | Primary key. |
| name | public."Name" | Unit of measure description. |
| modifieddate | timestamp |  |


## Table: production.workorder

**Description:** Manufacturing work orders.

| Column | Type | Description |
|--------|------|-------------|
| workorderid | integer | Primary key for WorkOrder records. |
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| orderqty | integer | Product quantity to build. |
| scrappedqty | smallint | Quantity that failed inspection. |
| startdate | timestamp | Work order start date. |
| enddate | timestamp | Work order end date. |
| duedate | timestamp | Work order due date. |
| scrapreasonid | smallint | Reason for inspection failure. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_WorkOrder_EndDate" |  |
| CONSTRAINT | "CK_WorkOrder_OrderQty" |  |
| CONSTRAINT | "CK_WorkOrder_ScrappedQty" |  |


## Table: production.workorderrouting

**Description:** Work order details.

| Column | Type | Description |
|--------|------|-------------|
| workorderid | integer | Primary key. Foreign key to WorkOrder.WorkOrderID. |
| productid | integer | Primary key. Foreign key to Product.ProductID. |
| operationsequence | smallint | Primary key. Indicates the manufacturing process sequence. |
| locationid | smallint | Manufacturing location where the part is processed. Foreign key to Location.LocationID. |
| scheduledstartdate | timestamp | Planned manufacturing start date. |
| scheduledenddate | timestamp | Planned manufacturing end date. |
| actualstartdate | timestamp | Actual start date. |
| actualenddate | timestamp | Actual end date. |
| actualresourcehrs | numeric(9,4) | Number of manufacturing hours used. |
| plannedcost | numeric | Estimated manufacturing cost. |
| actualcost | numeric | Actual manufacturing cost. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_WorkOrderRouting_ActualCost" |  |
| CONSTRAINT | "CK_WorkOrderRouting_ActualEndDate" |  |
| CONSTRAINT | "CK_WorkOrderRouting_ActualResourceHrs" |  |
| CONSTRAINT | "CK_WorkOrderRouting_PlannedCost" |  |
| CONSTRAINT | "CK_WorkOrderRouting_ScheduledEndDate" |  |

