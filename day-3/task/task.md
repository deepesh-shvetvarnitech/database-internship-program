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
#![alt text](<Screenshot 2026-08-03 192900.png>)
--LECT product_name ,category ,price  FROM product;/*
# [alt text](<Screenshot 2026-08-03 193158.png>)
--LECT * FROM product ORDER BY price ASC;
# [alt text](<Screenshot 2026-08-03 193517.png>)
--LECT * FROM product ORDER BY price DESC;
#[alt text](<Screenshot 2026-08-03 193737.png>)
--LECT * FROM product ORDER BY price DESC LIMIT 3;
 lt text](<Screenshot 2026-08-03 193836.png>)
--LECT DISTINCT category FROM product;
![alt text](<Screenshot 2026-08-03 194003.png>)

--LECT * FROM product WHERE product_name  LIKE 'm%';
#![alt text](<Screenshot 2026-08-03 195403.png>)
--LECT * FROM product WHERE brand IN ('dell','logitech');
![alt text](<Screenshot 2026-08-03 195618.png>)

--LECT * FROM product WHERE price  BETWEEN 1000 AND 20000;
![alt text](<Screenshot 2026-08-03 195749.png>)
SELECT * FROM product WHERE category  = 'electronics';
![alt text](<Screenshot 2026-08-03 195932.png>)
SELECT * FROM product WHERE stock < 20 ;
#![alt text](<Screenshot 2026-08-03 200029.png>)

SELECT * FROM product ORDER BY category , product_name;
![alt text](<Screenshot 2026-08-03 200205.png>)

SELECT * FROM product  WHERE brand LIKE 'l%'
![alt text](<Screenshot 2026-08-03 200744.png>)

SELECT * FROM product ORDER BY stock DESC LIMIT 5;
![alt text](<Screenshot 2026-08-03 201004.png>)

SELECT * FROM product WHERE category IN ('electronic', 'furniture');
# ![alt text](<Screenshot 2026-08-03 201133.png>)
SELECT * FROM product WHERE price > 10000 ORDER BY price DESC;
#  ![alt text](<Screenshot 2026-08-03 201323.png>)







