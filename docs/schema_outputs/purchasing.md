## Table: purchasing.purchaseorderdetail

**Description:** Individual products associated with a specific purchase order. See PurchaseOrderHeader.

| Column | Type | Description |
|--------|------|-------------|
| purchaseorderid | integer | Primary key. Foreign key to PurchaseOrderHeader.PurchaseOrderID. |
| purchaseorderdetailid | integer | Primary key. One line number per purchased product. |
| duedate | timestamp | Date the product is expected to be received. |
| orderqty | smallint | Quantity ordered. |
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| unitprice | numeric |  |
| receivedqty | numeric(8,2) | Quantity actually received from the vendor. |
| rejectedqty | numeric(8,2) | Quantity rejected during inspection. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_PurchaseOrderDetail_OrderQty" |  |
| CONSTRAINT | "CK_PurchaseOrderDetail_ReceivedQty" |  |
| CONSTRAINT | "CK_PurchaseOrderDetail_RejectedQty" |  |
| CONSTRAINT | "CK_PurchaseOrderDetail_UnitPrice" |  |


## Table: purchasing.purchaseorderheader

**Description:** General purchase order information. See PurchaseOrderDetail.

| Column | Type | Description |
|--------|------|-------------|
| purchaseorderid | integer | Primary key. |
| revisionnumber | smallint | Incremental number to track changes to the purchase order over time. |
| status | smallint | Order current status. 1 = Pending; 2 = Approved; 3 = Rejected; 4 = Complete |
| employeeid | integer | Employee who created the purchase order. Foreign key to Employee.BusinessEntityID. |
| vendorid | integer | Vendor with whom the purchase order is placed. Foreign key to Vendor.BusinessEntityID. |
| shipmethodid | integer | Shipping method. Foreign key to ShipMethod.ShipMethodID. |
| orderdate | timestamp | Purchase order creation date. |
| shipdate | timestamp | Estimated shipment date from the vendor. |
| subtotal | numeric | Purchase order subtotal. Computed as SUM(PurchaseOrderDetail.LineTotal)for the appropriate PurchaseOrderID. |
| taxamt | numeric | Tax amount. |
| freight | numeric | Shipping cost. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_PurchaseOrderHeader_Freight" |  |
| CONSTRAINT | "CK_PurchaseOrderHeader_ShipDate" |  |
| CONSTRAINT | "CK_PurchaseOrderHeader_Status" |  |
| CONSTRAINT | "CK_PurchaseOrderHeader_SubTotal" |  |
| CONSTRAINT | "CK_PurchaseOrderHeader_TaxAmt" |  |


## Table: purchasing.productvendor

**Description:** Cross-reference table mapping vendors with the products they supply.

| Column | Type | Description |
|--------|------|-------------|
| productid | integer | Primary key. Foreign key to Product.ProductID. |
| businessentityid | integer | Primary key. Foreign key to Vendor.BusinessEntityID. |
| averageleadtime | integer | The average span of time (in days) between placing an order with the vendor and receiving the purchased product. |
| standardprice | numeric |  |
| lastreceiptcost | numeric | The selling price when last purchased. |
| lastreceiptdate | timestamp | Date the product was last received by the vendor. |
| minorderqty | integer | The maximum quantity that should be ordered. |
| maxorderqty | integer | The minimum quantity that should be ordered. |
| onorderqty | integer | The quantity currently on order. |
| unitmeasurecode | character(3) |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_ProductVendor_AverageLeadTime" |  |
| CONSTRAINT | "CK_ProductVendor_LastReceiptCost" |  |
| CONSTRAINT | "CK_ProductVendor_MaxOrderQty" |  |
| CONSTRAINT | "CK_ProductVendor_MinOrderQty" |  |
| CONSTRAINT | "CK_ProductVendor_OnOrderQty" |  |
| CONSTRAINT | "CK_ProductVendor_StandardPrice" |  |


## Table: purchasing.shipmethod

**Description:** Shipping company lookup table.

| Column | Type | Description |
|--------|------|-------------|
| shipmethodid | integer | Primary key for ShipMethod records. |
| name | public."Name" | Shipping company name. |
| shipbase | numeric | Minimum shipping charge. |
| shiprate | numeric | Shipping charge per pound. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_ShipMethod_ShipBase" |  |
| CONSTRAINT | "CK_ShipMethod_ShipRate" |  |


## Table: purchasing.vendor

**Description:** Companies from whom Adventure Works Cycles purchases parts or other goods.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key for Vendor records.  Foreign key to BusinessEntity.BusinessEntityID |
| accountnumber | public."AccountNumber" | Vendor account (identification) number. |
| name | public."Name" | Company name. |
| creditrating | smallint | 1 = Superior, 2 = Excellent, 3 = Above average, 4 = Average, 5 = Below average |
| preferredvendorstatus | public."Flag" | 0 = Do not use if another vendor is available. 1 = Preferred over other vendors supplying the same product. |
| activeflag | public."Flag" | 0 = Vendor no longer used. 1 = Vendor is actively used. |
| purchasingwebserviceurl | character | Vendor URL. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_Vendor_CreditRating" |  |

