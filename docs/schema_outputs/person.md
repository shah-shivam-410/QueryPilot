## Table: person.address

**Description:** Street address information for customers, employees, and vendors.

| Column | Type | Description |
|--------|------|-------------|
| addressid | integer | Primary key for Address records. |
| addressline1 | character | First street address line. |
| addressline2 | character | Second street address line. |
| city | character | Name of the city. |
| stateprovinceid | integer | Unique identification number for the state or province. Foreign key to StateProvince table. |
| postalcode | character | Postal code for the street address. |
| spatiallocation | character | Latitude and longitude of this address. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: person.businessentityaddress

**Description:** Cross-reference table mapping customers, vendors, and employees to their addresses.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key. Foreign key to BusinessEntity.BusinessEntityID. |
| addressid | integer | Primary key. Foreign key to Address.AddressID. |
| addresstypeid | integer | Primary key. Foreign key to AddressType.AddressTypeID. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: person.countryregion

**Description:** Lookup table containing the ISO standard codes for countries and regions.

| Column | Type | Description |
|--------|------|-------------|
| countryregioncode | character | ISO standard code for countries and regions. |
| name | public."Name" | Country or region name. |
| modifieddate | timestamp |  |


## Table: person.emailaddress

**Description:** Where to send a person email.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key. Person associated with this email address.  Foreign key to Person.BusinessEntityID |
| emailaddressid | integer | Primary key. ID of this email address. |
| emailaddress | character | E-mail address for the person. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: person.person

**Description:** Human beings involved with AdventureWorks: employees, customer contacts, and vendor contacts.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key for Person records. |
| persontype | character(2) | Primary type of person: SC = Store Contact, IN = Individual (retail) customer, SP = Sales person, EM = Employee (non-sales), VC = Vendor contact, GC = General contact |
| namestyle | public."NameStyle" | 0 = The data in FirstName and LastName are stored in western style (first name, last name) order.  1 = Eastern style (last name, first name) order. |
| title | character | A courtesy title. For example, Mr. or Ms. |
| firstname | public."Name" | First name of the person. |
| middlename | public."Name" | Middle name or middle initial of the person. |
| lastname | public."Name" | Last name of the person. |
| suffix | character | Surname suffix. For example, Sr. or Jr. |
| emailpromotion | integer | 0 = Contact does not wish to receive e-mail promotions, 1 = Contact does wish to receive e-mail promotions from AdventureWorks, 2 = Contact does wish to receive e-mail promotions from AdventureWorks and selected partners. |
| additionalcontactinfo | xml | Additional contact information about the person stored in xml format. |
| demographics | xml | Personal information such as hobbies, and income collected from online shoppers. Used for sales analysis. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_Person_EmailPromotion" |  |
| CONSTRAINT | "CK_Person_PersonType" |  |


## Table: person.personphone

**Description:** Telephone number and type of a person.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Business entity identification number. Foreign key to Person.BusinessEntityID. |
| phonenumber | public."Phone" | Telephone number identification number. |
| phonenumbertypeid | integer | Kind of phone number. Foreign key to PhoneNumberType.PhoneNumberTypeID. |
| modifieddate | timestamp |  |


## Table: person.phonenumbertype

**Description:** Type of phone number of a person.

| Column | Type | Description |
|--------|------|-------------|
| phonenumbertypeid | integer | Primary key for telephone number type records. |
| name | public."Name" | Name of the telephone number type |
| modifieddate | timestamp |  |


## Table: person.stateprovince

**Description:** State and province lookup table.

| Column | Type | Description |
|--------|------|-------------|
| stateprovinceid | integer | Primary key for StateProvince records. |
| stateprovincecode | character(3) | ISO standard state or province code. |
| countryregioncode | character | ISO standard country or region code. Foreign key to CountryRegion.CountryRegionCode. |
| isonlystateprovinceflag | public."Flag" | 0 = StateProvinceCode exists. 1 = StateProvinceCode unavailable, using CountryRegionCode. |
| name | public."Name" | State or province description. |
| territoryid | integer | ID of the territory in which the state or province is located. Foreign key to SalesTerritory.SalesTerritoryID. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: person.addresstype

**Description:** Types of addresses stored in the Address table.

| Column | Type | Description |
|--------|------|-------------|
| addresstypeid | integer | Primary key for AddressType records. |
| name | public."Name" | Address type description. For example, Billing, Home, or Shipping. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: person.businessentity

**Description:** Source of the ID that connects vendors, customers, and employees with address and contact information.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key for all customers, vendors, and employees. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: person.businessentitycontact

**Description:** Cross-reference table mapping stores, vendors, and employees to people

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key. Foreign key to BusinessEntity.BusinessEntityID. |
| personid | integer | Primary key. Foreign key to Person.BusinessEntityID. |
| contacttypeid | integer | Primary key.  Foreign key to ContactType.ContactTypeID. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |


## Table: person.contacttype

**Description:** Lookup table containing the types of business entity contacts.

| Column | Type | Description |
|--------|------|-------------|
| contacttypeid | integer | Primary key for ContactType records. |
| name | public."Name" | Contact type description. |
| modifieddate | timestamp |  |


## Table: person.password

**Description:** One way hashed authentication information

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer |  |
| passwordhash | character | Password for the e-mail account. |
| passwordsalt | character | Random value concatenated with the password string before the password is hashed. |
| rowguid | uuid |  |
| modifieddate | timestamp |  |

