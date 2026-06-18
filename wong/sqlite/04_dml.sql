-- Add a new customer representing yourself with appropriate but fictitious details to the Customers table
insert into Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) 
values  ("92", "John Pork Ltd.", "Pohn Jork", "41 Sicks-Sevuhn Drive", "OpolisTopolis", "02143", "Uganda");

-- Add a new category of product, Expedition supplies
insert into Categories (CategoryID, CategoryName, Description)
values  ("9", "Expedition Supplies", "Supplies for expeditions");

-- Decide on what type of expedition you propose to undertake, and add appropriate equipment to the products table. 
-- You will also need to add one or more suppliers or use one of the existing ones.
insert into Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
values ("78", "Blue Contacts", "2", "9", "2 contacts", "67");

insert into Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
values ("79", "Blonde Wig", "3", "9", "41 wigs", "67");

insert into Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
values ("80", "Hat", "4", "9", "6 hats", "67");

insert into Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
values ("81", "Sword", "1", "9", "2 swords", "67");

insert into Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
values ("82", "Triforce", "3", "9", "6 hats", "67");

insert into Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
values ("83", "Peace Symbol Sequins", "7", "9", "4100 Sequins", "67");

insert into Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
values ("84", "Calc (Short for Calculator)", "7", "9", "3", "41");

-- Add a customer order with yourself as a customer 
insert into Orders (CustomerID, EmployeeID, OrderDate, ShipperID)
values ("92", "10", "1967-4-1", "2");

-- Add appropriate order details to add the items you need for the expedition to the order
insert into OrderDetails (OrderID, ProductID, Quantity)
values ("519", "10444", "78", "6");

insert into OrderDetails (OrderID, ProductID, Quantity)
values ("520", "10444", "79", "7");

insert into OrderDetails (OrderID, ProductID, Quantity)
values ("521", "10444", "80", "6");

insert into OrderDetails (OrderID, ProductID, Quantity)
values ("522", "10444", "81", "7");

insert into OrderDetails (OrderID, ProductID, Quantity)
values ("523", "10444", "82", "6");

insert into OrderDetails (OrderID, ProductID, Quantity)
values ("524", "10444", "83", "7");

insert into OrderDetails (OrderID, ProductID, Quantity)
values ("525", "10444", "84", "6");

-- Create a SQL Query which shows the items you have ordered with their total costs
select
	p.ProductName,
	od.Quantity * p.Price as "Total Cost"
from OrderDetails as od
join Products as p
on p.ProductID = od.ProductID
where od.OrderID = "10444";


-- Now update the products table to increase all of your prices by 10% and rerun the query.
update Products
set Price = Price * 1.1 
where ProductID > 77;

select
	p.ProductName,
	od.Quantity * p.Price as "Total Cost"
from OrderDetails as od
join Products as p
on p.ProductID = od.ProductID
where od.OrderID = "10444";

-- Delete all the data you have added to the database. You will need to start with the tables that have foreign keys. 

delete from OrderDetails where OrderID = 10444;
delete from Products where ProductID > 77;
delete from Orders where OrderID = 10444;
delete from Categories where CategoryID = 9;
delete from Customers where CustomerID = 92;