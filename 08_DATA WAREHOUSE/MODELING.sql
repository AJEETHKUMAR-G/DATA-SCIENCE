CREATE DATABASE sales_model;

CREATE TABLE sales_model.Orders(
 OrderID INT,
    OrderDate DATE,
    CustomerID INT,
    CustomerName VARCHAR(100),
    CustomerEmail VARCHAR(100),
    ProductID INT,
    ProductName VARCHAR(100),
    ProductCategory VARCHAR(50),
    RegionID INT,
    RegionName VARCHAR(50),
    Country VARCHAR(50),
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    TotalAmount DECIMAL(10,2)
);

INSERT INTO sales_model.Orders (OrderID, OrderDate, CustomerID, CustomerName, CustomerEmail, ProductID, ProductName, ProductCategory, RegionID, RegionName, Country, Quantity, UnitPrice, TotalAmount) 
VALUES 
(1, '2024-02-01', 101, 'Alice Johnson', 'alice@example.com', 201, 'Laptop', 'Electronics', 301, 'North America', 'USA', 2, 800.00, 1600.00),
(2, '2024-02-02', 102, 'Bob Smith', 'bob@example.com', 202, 'Smartphone', 'Electronics', 302, 'Europe', 'Germany', 1, 500.00, 500.00),
(3, '2024-02-03', 103, 'Charlie Brown', 'charlie@example.com', 203, 'Tablet', 'Electronics', 303, 'Asia', 'India', 3, 300.00, 900.00),
(4, '2024-02-04', 101, 'Alice Johnson', 'alice@example.com', 204, 'Headphones', 'Accessories', 301, 'North America', 'USA', 1, 150.00, 150.00),
(5, '2024-02-05', 104, 'David Lee', 'david@example.com', 205, 'Gaming Console', 'Electronics', 302, 'Europe', 'France', 1, 400.00, 400.00),
(6, '2024-02-06', 102, 'Bob Smith', 'bob@example.com', 206, 'Smartwatch', 'Electronics', 303, 'Asia', 'China', 2, 200.00, 400.00),
(7, '2024-02-07', 105, 'Eve Adams', 'eve@example.com', 201, 'Laptop', 'Electronics', 301, 'North America', 'Canada', 1, 800.00, 800.00),
(8, '2024-02-08', 106, 'Frank Miller', 'frank@example.com', 207, 'Monitor', 'Accessories', 302, 'Europe', 'Italy', 2, 250.00, 500.00),
(9, '2024-02-09', 107, 'Grace White', 'grace@example.com', 208, 'Keyboard', 'Accessories', 303, 'Asia', 'Japan', 3, 100.00, 300.00),
(10, '2024-02-10', 104, 'David Lee', 'david@example.com', 209, 'Mouse', 'Accessories', 301, 'North America', 'USA', 1, 50.00, 50.00);

SELECT * FROM sales_model.orders;

DROP DATABASE IF EXISTS orders_model;
CREATE DATABASE orders_model;

CREATE TABLE orders_model.staging_sales AS
SELECT * FROM sales_model.orders;

SELECT * FROM orders_model.staging_sales;

CREATE VIEW orders_model.transform_sales
 AS SELECT * FROM orders_model.staging_sales
 WHERE quantity IS NOT NULL;
 
 -- CUSTOMERS, PRODUCTS, REGIONS
 
 SELECT DISTINCT(customerID), customerName, customerEmail 
 FROM orders_model.transform_sales;
 
 SELECT *, ROW_NUMBER() OVER(ORDER BY T.customerId)
 AS surrogate_customer_key
 FROM
 (SELECT DISTINCT(customerID), customerName, customerEmail 
 FROM orders_model.transform_sales) AS T;
 
 CREATE VIEW orders_model.view_DimCustomer AS
 SELECT *, ROW_NUMBER() OVER(ORDER BY T.customerId)
 AS surrogate_customer_key
 FROM
 (SELECT DISTINCT(customerID), customerName, customerEmail 
 FROM orders_model.transform_sales) AS T;
 
 CREATE TABLE orders_model.DimCustomers(
 customerID INT,
 customerName VARCHAR(30),
 customerEmail VARCHAR(100),
 surr_customer INT
 );
 
 INSERT INTO orders_model.DimCustomers
 SELECT * FROM orders_model.view_Dimcustomer;
 
 SELECT * FROM orders_model.DimCustomers;
 
 
 SELECT *, 
ROW_NUMBER() OVER(ORDER BY T.ProductID )AS Surrogate_dim_product
FROM (SELECT DISTINCT(ProductID),ProductName,ProductCategory 
FROM orders_model.transform_sales) AS T;
 
 
 CREATE TABLE orders_model.DimProducts(
    ProductID INT,
    ProductName VARCHAR(200),
    ProductCategory VARCHAR(200),
    Surrogate_dim_product INT
);

CREATE VIEW orders_model.DimProductsView AS 
SELECT *, 
ROW_NUMBER() OVER(ORDER BY T.ProductID )AS Surrogate_dim_product
 FROM (SELECT DISTINCT(ProductID),ProductName,ProductCategory 
FROM orders_model.transform_sales) AS T;

INSERT INTO orders_model.DimProducts
SELECT * FROM orders_model.DimProductsView;

SELECT * FROM orders_model.DimProducts;

CREATE VIEW orders_model.DimRegionsView AS 
SELECT *, 
ROW_NUMBER() OVER(ORDER BY T.RegionID )AS Surrogate_dim_region
 FROM (SELECT DISTINCT(RegionID),RegionName,Country
FROM orders_model.transform_sales) AS T;

CREATE TABLE orders_model.DimRegion (
    RegionID INT,
    RegionName VARCHAR(20),
    Country VARCHAR(20),
    Surrogate_dim_region INT
);

INSERT INTO orders_model.dimregion
SELECT * FROM orders_model.DimRegionsView;

SELECT * FROM orders_model.dimregion;

SELECT * FROM orders_model.transform_Sales;

CREATE VIEW orders_model.dimOrderDateView AS
SELECT *, ROW_NUMBER() OVER(ORDER BY T.orderDate) AS Surrogate_dim_orderdate FROM
(SELECT DISTINCT orderDate FROM orders_model.transform_sales) AS T;
CREATE TABLE orders_model.dimOrderDate(
    orderDate DATE,
    Surrogate_dim_orderdate INT
);
INSERT INTO orders_model.dimorderdate
SELECT * FROM orders_model.dimOrderDateView;
CREATE TABLE orders_model.fact_sales(
orderID INT,
quantity INT,
UnitPrice DECIMAL(10,2),
TotalAmount DECIMAL(10,2),
customerID INT,productID INT, RegionID INT
,OrderdateID INT
);

SELECT 
orderID,Quantity,UnitPrice,TotalAmount,DC.surr_customer,DP.Surrogate_dim_product,
DR.surrogate_dim_region,DOD.surrogate_dim_orderdate
FROM orders_model.transform_sales F
LEFT JOIN orders_model.dimcustomers DC
ON F.customerID = DC.customerID
LEFT JOIN orders_model.Dimproducts DP
ON F.productID = DP.productID
LEFT JOIN orders_model.dimregion DR
ON F.country = DR.country
LEFT JOIN orders_model.dimorderdate DOD
on F.orderDate = DOD.orderDate;

INSERT INTO orders_model.fact_sales
SELECT 
orderID,Quantity,UnitPrice,TotalAmount,DC.surr_customer,DP.Surrogate_dim_product,
DR.surrogate_dim_region,DOD.surrogate_dim_orderdate
FROM orders_model.transform_sales F
LEFT JOIN orders_model.dimcustomers DC
ON F.customerID = DC.customerID
LEFT JOIN orders_model.Dimproducts DP
ON F.productID = DP.productID
LEFT JOIN orders_model.dimregion DR
ON F.country = DR.country
LEFT JOIN orders_model.dimorderdate DOD
on F.orderDate = DOD.orderDate;