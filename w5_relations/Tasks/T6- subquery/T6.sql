 SELECT FirstName, LastName FROM Employee
 WHERE ReportsTo = (SELECT EmployeeId FROM Employee WHERE FirstName = 'Nancy' AND LastName = 'Edwards') ORDER BY FirstName, LastName;