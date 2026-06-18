-- List the number of customers in each country ordered alphabetically by country
select Country, count(*) from Customers as cm group by cm.Country order by Country; 

-- For each order list the orderid, orderdate, customername and total cost
select distinct
    o.OrderID, 
    o.OrderDate, 
    c.CustomerName, 
    (od.Quantity * p.Price) as total_cost
from Orders as o
join Customers as c
    on o.CustomerID = c.CustomerID
join OrderDetails as od
    on o.OrderID = od.OrderID
join Products as p
    on od.ProductID = p.ProductID;


-- Amend the query above so that only orders with a total cost > 400 are shown
select
    o.OrderID, 
    o.OrderDate, 
    c.CustomerName,
	sum(od.Quantity * p.Price) as total_cost
from Orders as o
join Customers as c
    on o.CustomerID = c.CustomerID
join OrderDetails as od
    on o.OrderID = od.OrderID
join Products as p
    on od.ProductID = p.ProductID
group by c.CustomerName
having total_cost > 400;


-- Show how many orders there are on each order date
select
    o.OrderDate,
    count(*)
from Orders as o
group by o.OrderDate;

-- For each customer show the minimum, maximum and average price of products they have ordered
select
    c.CustomerName,
    min(od.Quantity * p.Price) as mn,
    max(od.Quantity * p.Price) as mx,
    avg(od.Quantity * p.Price) as vg
from Customers as c
join Orders as o
    on o.CustomerID = c.CustomerID
join OrderDetails as od
    on od.OrderID = o.OrderID
join Products as p
    on p.ProductID = od.ProductID
group by c.CustomerName;

-- How many orders has each employee processed. Order by their name.
select 
    e.FirstName || e.LastName,
    count(o.OrderID)
from Employees as e
left join Orders as o
    on o.EmployeeID = e.EmployeeID
group by e.FirstName;

-- Find the total Quantity of items sold by Category
select
    CategoryName,
	Quantity
from Categories as c
join Products as p
    on c.CategoryID = p.CategoryID
join OrderDetails as od
    on p.ProductID = od.ProductID
group by c.CategoryName;

-- Find suppliers who sell more than three products
select 
	SupplierName,
	count(ProductName) as numProductsSold
from Suppliers as s
join Products as p
    on s.SupplierID = p.SupplierID
group by SupplierName
having numProductsSold > 3;
 
-- List all customers and the total number of orders they have placed (including those with zero orders)

select 
	c.CustomerName,
	count(o.CustomerID) as numOrders
from Customers as c
left join Orders as o
	on c.CustomerID = o.CustomerID
group by o.CustomerID	