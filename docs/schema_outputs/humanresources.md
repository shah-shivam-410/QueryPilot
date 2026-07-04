## Table: humanresources.department

**Description:** Lookup table containing the departments within the Adventure Works Cycles company.

| Column | Type | Description |
|--------|------|-------------|
| departmentid | integer | Primary key for Department records. |
| name | public."Name" | Name of the department. |
| groupname | public."Name" | Name of the group to which the department belongs. |
| modifieddate | timestamp |  |


## Table: humanresources.employee

**Description:** Employee information such as salary, department, and title.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Primary key for Employee records.  Foreign key to BusinessEntity.BusinessEntityID. |
| nationalidnumber | character | Unique national identification number such as a social security number. |
| loginid | character | Network login. |
| jobtitle | character | Work title such as Buyer or Sales Representative. |
| birthdate | date | Date of birth. |
| maritalstatus | character(1) | M = Married, S = Single |
| gender | character(1) | M = Male, F = Female |
| hiredate | date | Employee hired on this date. |
| salariedflag | public."Flag" | Job classification. 0 = Hourly, not exempt from collective bargaining. 1 = Salaried, exempt from collective bargaining. |
| vacationhours | smallint | Number of available vacation hours. |
| sickleavehours | smallint | Number of available sick leave hours. |
| currentflag | public."Flag" | 0 = Inactive, 1 = Active |
| rowguid | uuid |  |
| modifieddate | timestamp |  |
| organizationnode | character | Where the employee is located in corporate hierarchy. |
| CONSTRAINT | "CK_Employee_BirthDate" |  |
| CONSTRAINT | "CK_Employee_Gender" |  |
| CONSTRAINT | "CK_Employee_HireDate" |  |
| CONSTRAINT | "CK_Employee_MaritalStatus" |  |
| CONSTRAINT | "CK_Employee_SickLeaveHours" |  |
| CONSTRAINT | "CK_Employee_VacationHours" |  |


## Table: humanresources.employeedepartmenthistory

**Description:** Employee department transfers.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Employee identification number. Foreign key to Employee.BusinessEntityID. |
| departmentid | smallint | Department in which the employee worked including currently. Foreign key to Department.DepartmentID. |
| shiftid | smallint | Identifies which 8-hour shift the employee works. Foreign key to Shift.Shift.ID. |
| startdate | date | Date the employee started work in the department. |
| enddate | date | Date the employee left the department. NULL = Current department. |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_EmployeeDepartmentHistory_EndDate" |  |


## Table: humanresources.employeepayhistory

**Description:** Employee pay history.

| Column | Type | Description |
|--------|------|-------------|
| businessentityid | integer | Employee identification number. Foreign key to Employee.BusinessEntityID. |
| ratechangedate | timestamp | Date the change in pay is effective |
| rate | numeric | Salary hourly rate. |
| payfrequency | smallint | 1 = Salary received monthly, 2 = Salary received biweekly |
| modifieddate | timestamp |  |
| CONSTRAINT | "CK_EmployeePayHistory_PayFrequency" |  |
| CONSTRAINT | "CK_EmployeePayHistory_Rate" |  |


## Table: humanresources.jobcandidate

**Description:** RÃ©sumÃ©s submitted to Human Resources by job applicants.

| Column | Type | Description |
|--------|------|-------------|
| jobcandidateid | integer | Primary key for JobCandidate records. |
| businessentityid | integer | Employee identification number if applicant was hired. Foreign key to Employee.BusinessEntityID. |
| resume | xml | RÃ©sumÃ© in XML format. |
| modifieddate | timestamp |  |


## Table: humanresources.shift

**Description:** Work shift lookup table.

| Column | Type | Description |
|--------|------|-------------|
| shiftid | integer | Primary key for Shift records. |
| name | public."Name" | Shift description. |
| starttime | time | Shift start time. |
| endtime | time | Shift end time. |
| modifieddate | timestamp |  |

