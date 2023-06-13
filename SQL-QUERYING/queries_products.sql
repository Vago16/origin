
--1. A chair with a price of 44.00 that can not be returned
INSERT INTO products (name, price, can_be_returned)
VALUES ('chair', 44.00, 'f'); 
--2. A stool with a price of 25.99 and can be returned
INSERT INTO products (name, price, can_be_returned)
VALUES ('stool', 25.99, 't');
--3. A table with a price of 124.00 and can not be returned
INSERT INTO products (name, price, can_be_returned)
VALUES ('table', 124.00, 'f');
--4. Display all rows and columns of table
SELECT *
FROM products;
--5. Display names of all the products
SELECT name
FROM products;
--6.Display all names and prices of products
SELECT name, price
FROM products;
--7.Adding a lamp with a price of 950.00 and can not be returned
INSERT INTO products (name, price, can_be_returned)
VALUES ('lamp', 950.00, 'f');
--8.Displays only products that can be returned
SeLECT *
FROM products
WHERE can_be_returned = 't';
--9. Displays only products that are less than 44.00
SELECT *
FROM products
WHERE price < 44.00;
--10. Displays only products between 22.50 and 99.99  in price
SELECT *
FROM products
WHERE price BETWEEN 22.50 AMD 99.99;
--11. Update everything to be 20.00 off
UPDATE products 
SET price = price - 20.00;
--12. Update everything that is less than 25.00 to be sold out
DELETE FROM products
WHERE price < 25;
--13. Remaining products have their price raised by 20.00
UPDATE products
SET price = price + 20.00;
--14. Now all products are returnable
Update products
SET can_be_returned = 't';




