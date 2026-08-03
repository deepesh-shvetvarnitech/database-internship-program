CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

INSERT INTO product(product_id,product_name,category,brand,price,stock) VALUES
(1,'laptop' , 'electronics' , 'dell', 65000,12),
(2, 'keybord' , 'electronics','logitech',1200,45),

(3,'mouse', 'electronics', 'logitech',800,60),
(4,'office chair','furniture', 'greensoul',7500,18),
(5,'study table' ,'furniture', 'ikea',9500 ,10),
(6,'notebook' , 'stationary ' , 'classmate' ,80,150),
(7, 'pan pack ' , 'stationary' ,'cello', 120,220),
(8, 'monitor' , 'electronics','dell',18000,20);

--SELECT * FROM product;
--LECT product_name ,category ,price  FROM product;/*
--LECT * FROM product ORDER BY price ASC;
--LECT * FROM product ORDER BY price DESC;
--LECT * FROM product ORDER BY price DESC LIMIT 3;
--LECT DISTINCT category FROM product;

--LECT * FROM product WHERE product_name  LIKE 'm%';
--LECT * FROM product WHERE brand IN ('dell','logitech');

--LECT * FROM product WHERE price  BETWEEN 1000 AND 20000;
SELECT * FROM product WHERE category  = 'electronics';
SELECT * FROM product WHERE stock < 20 ;

--LECT * FROM product ORDER BY category , product_name;

SELECT * FROM product  WHERE brand LIKE 'l%'

SELECT * FROM product ORDER BY stock DESC LIMIT 5;

SELECT * FROM product WHERE category IN ('electronic', 'furniture');

SELECT * FROM product WHERE price > 10000 ORDER BY price DESC;





