## Table: sales.customer

**Description:** Current customer information. Also see the Person and Store tables.

| Column | Type | Description |
|--------|------|-------------|
| customerid | integer | Primary key. |
| personid | integer | Foreign key to Person.BusinessEntityID |
| storeid | integer | Foreign key to Store.BusinessEntityID |
| territoryid | integer | ID of the territory in which the customer is located. Foreign key to SalesTerritory.SalesTerritoryID. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: sales.creditcard

**Description:** Customer credit card information.

| Column | Type | Description |
|--------|------|-------------|
| creditcardid | integer | Primary key for CreditCard records. |
| cardtype | character | Credit card name. |
| cardnumber | character | Credit card number. |
| expmonth | smallint | Credit card expiration month. |
| expyear | smallint | Credit card expiration year. |
| modifieddate | timestamp |  |


## Table: sales.currencyrate

**Description:** Currency exchange rates.

| Column | Type | Description |
|--------|------|-------------|
| currencyrateid | integer | Primary key for CurrencyRate records. |
| currencyratedate | timestamp | Date and time the exchange rate was obtained. |
| fromcurrencycode | character(3) | Exchange rate was converted from this currency code. |
| tocurrencycode | character(3) | Exchange rate was converted to this currency code. |
| averagerate | numeric | Average exchange rate for the day. |
| endofdayrate | numeric | Final exchange rate for the day. |
| modifieddate | timestamp |  |


## Table: sales.countryregioncurrency

**Description:** Cross-reference table mapping ISO currency codes to a country or region.

| Column | Type | Description |
|--------|------|-------------|
| countryregioncode | character | ISO code for countries and regions. Foreign key to CountryRegion.CountryRegionCode. |
| currencycode | character(3) | ISO standard currency code. Foreign key to Currency.CurrencyCode. |
| modifieddate | timestamp |  |


## Table: sales.currency

**Description:** Lookup table containing standard ISO currencies.

| Column | Type | Description |
|--------|------|-------------|
| currencycode | character(3) | The ISO code for the Currency. |
| name | public."Name" | Currency name. |
| modifieddate | timestamp |  |


## Table: sales.personcreditcard

**Description:** Cross-reference table mapping people to their credit card information in the CreditCard table.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Business entity identification number. Foreign key to Person.BusinessEntityID. |
| creditcardid | integer | Credit card identification number. Foreign key to CreditCard.CreditCardID. |
| modifieddate | timestamp |  |


## Table: sales.store

**Description:** Customers (resellers) of Adventure Works products.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key. Foreign key to Customer.BusinessEntityID. |
| name | public."Name" | Name of the store. |
| salespersonid | integer | ID of the sales person assigned to the customer. Foreign key to SalesPerson.BusinessEntityID. |
| demographics | xml | Demographic informationg about the store such as the number of employees, annual sales and store type. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: sales.shoppingcartitem

**Description:** Contains online customer orders until the order is submitted or cancelled.

| Column | Type | Description |
|--------|------|-------------|
| shoppingcartitemid | integer | Primary key for ShoppingCartItem records. |
| shoppingcartid | character | Shopping cart identification number. |
| quantity | integer | Product quantity ordered. |
| productid | integer | Product ordered. Foreign key to Product.ProductID. |
| datecreated | timestamp | Date the time the record was created. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_ShoppingCartItem_Quantity" |  |


## Table: sales.specialoffer

**Description:** Sale discounts lookup table.

| Column | Type | Description |
|--------|------|-------------|
| specialofferid | integer | Primary key for SpecialOffer records. |
| description | character | Discount description. |
| discountpct | numeric | Discount precentage. |
| type | character | Discount type category. |
| category | character | Group the discount applies to such as Reseller or Customer. |
| startdate | timestamp | Discount start date. |
| enddate | timestamp | Discount end date. |
| minqty | integer | Minimum discount percent allowed. |
| maxqty | integer | Maximum discount percent allowed. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_SpecialOffer_DiscountPct" |  |
| CONSTRAINT | "CK_SpecialOffer_EndDate" |  |
| CONSTRAINT | "CK_SpecialOffer_MaxQty" |  |
| CONSTRAINT | "CK_SpecialOffer_MinQty" |  |


## Table: sales.salesorderdetail

**Description:** Individual products associated with a specific sales order. See SalesOrderHeader.

| Column | Type | Description |
|--------|------|-------------|
| salesorderid | integer | Primary key. Foreign key to SalesOrderHeader.SalesOrderID. |
| salesorderdetailid | integer | Primary key. One incremental unique number per product sold. |
| carriertrackingnumber | character | Shipment tracking number supplied by the shipper. |
| orderqty | smallint | Quantity ordered per product. |
| productid | integer | Product sold to customer. Foreign key to Product.ProductID. |
| specialofferid | integer | Promotional code. Foreign key to SpecialOffer.SpecialOfferID. |
| unitprice | numeric | Selling price of a single product. |
| unitpricediscount | numeric | Discount amount. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_SalesOrderDetail_OrderQty" |  |
| CONSTRAINT | "CK_SalesOrderDetail_UnitPrice" |  |
| CONSTRAINT | "CK_SalesOrderDetail_UnitPriceDiscount" |  |


## Table: sales.salesorderheader

**Description:** General sales order information.

| Column | Type | Description |
|--------|------|-------------|
| salesorderid | integer | Primary key. |
| revisionnumber | smallint | Incremental number to track changes to the sales order over time. |
| orderdate | timestamp | Dates the sales order was created. |
| duedate | timestamp | Date the order is due to the customer. |
| shipdate | timestamp | Date the order was shipped to the customer. |
| status | smallint | Order current status. 1 = In process; 2 = Approved; 3 = Backordered; 4 = Rejected; 5 = Shipped; 6 = Cancelled |
| onlineorderflag | public."Flag" | 0 = Order placed by sales person. 1 = Order placed online by customer. |
| purchaseordernumber | public."OrderNumber" | Customer purchase order number reference. |
| accountnumber | public."AccountNumber" | Financial accounting number reference. |
| customerid | integer | Customer identification number. Foreign key to Customer.BusinessEntityID. |
| salespersonid | integer | Sales person who created the sales order. Foreign key to SalesPerson.BusinessEntityID. |
| territoryid | integer | Territory in which the sale was made. Foreign key to SalesTerritory.SalesTerritoryID. |
| billtoaddressid | integer | Customer billing address. Foreign key to Address.AddressID. |
| shiptoaddressid | integer | Customer shipping address. Foreign key to Address.AddressID. |
| shipmethodid | integer | Shipping method. Foreign key to ShipMethod.ShipMethodID. |
| creditcardid | integer | Credit card identification number. Foreign key to CreditCard.CreditCardID. |
| creditcardapprovalcode | character | Approval code provided by the credit card company. |
| currencyrateid | integer | Currency exchange rate used. Foreign key to CurrencyRate.CurrencyRateID. |
| subtotal | numeric | Sales subtotal. Computed as SUM(SalesOrderDetail.LineTotal)for the appropriate SalesOrderID. |
| taxamt | numeric | Tax amount. |
| freight | numeric | Shipping cost. |
| totaldue | numeric | Total due from customer. Computed as Subtotal + TaxAmt + Freight. |
| comment | character | Sales representative comments. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_SalesOrderHeader_DueDate" |  |
| CONSTRAINT | "CK_SalesOrderHeader_Freight" |  |
| CONSTRAINT | "CK_SalesOrderHeader_ShipDate" |  |
| CONSTRAINT | "CK_SalesOrderHeader_Status" |  |
| CONSTRAINT | "CK_SalesOrderHeader_SubTotal" |  |
| CONSTRAINT | "CK_SalesOrderHeader_TaxAmt" |  |


## Table: sales.salesorderheadersalesreason

**Description:** Cross-reference table mapping sales orders to sales reason codes.

| Column | Type | Description |
|--------|------|-------------|
| salesorderid | integer | Primary key. Foreign key to SalesOrderHeader.SalesOrderID. |
| salesreasonid | integer | Primary key. Foreign key to SalesReason.SalesReasonID. |
| modifieddate | timestamp |  |


## Table: sales.specialofferproduct

**Description:** Cross-reference table mapping products to special offer discounts.

| Column | Type | Description |
|--------|------|-------------|
| specialofferid | integer | Primary key for SpecialOfferProduct records. |
| productid | integer | Product identification number. Foreign key to Product.ProductID. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: sales.salesperson

**Description:** Sales representative current information.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key for SalesPerson records. Foreign key to Employee.BusinessEntityID |
| territoryid | integer | Territory currently assigned to. Foreign key to SalesTerritory.SalesTerritoryID. |
| salesquota | numeric | Projected yearly sales. |
| bonus | numeric | Bonus due if quota is met. |
| commissionpct | numeric | Commision percent received per sale. |
| salesytd | numeric | Sales total year to date. |
| saleslastyear | numeric | Sales total of previous year. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_SalesPerson_Bonus" |  |
| CONSTRAINT | "CK_SalesPerson_CommissionPct" |  |
| CONSTRAINT | "CK_SalesPerson_SalesLastYear" |  |
| CONSTRAINT | "CK_SalesPerson_SalesQuota" |  |
| CONSTRAINT | "CK_SalesPerson_SalesYTD" |  |


## Table: sales.salespersonquotahistory

**Description:** Sales performance tracking.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Sales person identification number. Foreign key to SalesPerson.BusinessEntityID. |
| quotadate | timestamp | Sales quota date. |
| salesquota | numeric | Sales quota amount. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_SalesPersonQuotaHistory_SalesQuota" |  |


## Table: sales.salesreason

**Description:** Lookup table of customer purchase reasons.

| Column | Type | Description |
|--------|------|-------------|
| salesreasonid | integer | Primary key for SalesReason records. |
| name | public."Name" | Sales reason description. |
| reasontype | public."Name" | Category the sales reason belongs to. |
| modifieddate | timestamp |  |


## Table: sales.salesterritory

**Description:** Sales territory lookup table.

| Column | Type | Description |
|--------|------|-------------|
| territoryid | integer | Primary key for SalesTerritory records. |
| name | public."Name" | Sales territory description |
| countryregioncode | character | ISO standard country or region code. Foreign key to CountryRegion.CountryRegionCode. |
| "group" | character | Geographic area to which the sales territory belong. |
| salesytd | numeric | Sales in the territory year to date. |
| saleslastyear | numeric | Sales in the territory the previous year. |
| costytd | numeric | Business costs in the territory year to date. |
| costlastyear | numeric | Business costs in the territory the previous year. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_SalesTerritory_CostLastYear" |  |
| CONSTRAINT | "CK_SalesTerritory_CostYTD" |  |
| CONSTRAINT | "CK_SalesTerritory_SalesLastYear" |  |
| CONSTRAINT | "CK_SalesTerritory_SalesYTD" |  |


## Table: sales.salesterritoryhistory

**Description:** Sales representative transfers to other sales territories.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key. The sales rep.  Foreign key to SalesPerson.BusinessEntityID. |
| territoryid | integer | Primary key. Territory identification number. Foreign key to SalesTerritory.SalesTerritoryID. |
| startdate | timestamp | Primary key. Date the sales representive started work in the territory. |
| enddate | timestamp | Date the sales representative left work in the territory. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_SalesTerritoryHistory_EndDate" |  |


## Table: sales.salestaxrate

**Description:** Tax rate lookup table.

| Column | Type | Description |
|--------|------|-------------|
| salestaxrateid | integer | Primary key for SalesTaxRate records. |
| stateprovinceid | integer | State, province, or country/region the sales tax applies to. |
| taxtype | smallint | 1 = Tax applied to retail transactions, 2 = Tax applied to wholesale transactions, 3 = Tax applied to all sales (retail and wholesale) transactions. |
| taxrate | numeric | Tax rate amount. |
| name | public."Name" | Tax rate description. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_SalesTaxRate_TaxType" |  |

