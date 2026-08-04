CREATE TABLE appointments(
    appointment_id INT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    department  VARCHAR(50) NOT NULL,
    consultant_fee DECIMAL(10,2) NOT NULL,
    appointment_status VARCHAR(20) NOT NULL
);
INSERT INTO appointments (appointment_id,patient_name,doctor_name,department,consultant_fee,appointment_status) VALUES
(1 ,	'Rahul',	'Dr. Sharma'	,'Cardiology',	800,	'Completed'),
(2	,'Priya'	,'Dr. Mehta',	'Dermatology',	600,	'Completed'),
(3	,'Aman',	'Dr. Sharma',	'Cardiology'	,800	,'Pending'),
(4	,'Neha',	'Dr. Patel',	'Orthopedic'	,1200,	'Completed'),
(5,	'Rohan',	'Dr. Khan',	'Neurology',	1500,	'Cancelled'),
(6,	'Anjali'	,'Dr. Mehta',	'Dermatology',	600	,'Completed'),
(7,	'Karan',	'Dr. Patel',	'Orthopedic',	1200	,'Pending'),
(8,	'Sneha',	'Dr. Khan',	'Neurology',	1500,	'Completed');

SELECT * FROM appointments;
# ![alt text](<Screenshot 2026-08-04 192029.png>)

SELECT patient_name,doctor_name,consultant_fee FROM appointments;
# ![alt text](<Screenshot 2026-08-04 192341.png>)
SELECT * FROM appointments WHERE department IN ('Cardiology','Neurology');
# ![alt text](<Screenshot 2026-08-04 192602.png>)

SELECT * FROM appointments WHERE patient_name LIKE 'A%';
# ![alt text](<Screenshot 2026-08-04 192752.png>)

SELECT * FROM appointments WHERE consultant_fee BETWEEN 700 AND 1300;
# ![alt text](<Screenshot 2026-08-04 192957.png>)
SELECT * FROM appointments  ORDER BY consultant_fee   ASC ;
# ![alt text](<Screenshot 2026-08-04 192957-1.png>)
SELECT * FROM appointments  ORDER BY consultant_fee   DESC LIMIT 3;
# ![alt text](<Screenshot 2026-08-04 193330.png>)
SELECT COUNT (*) AS "Total Appintments" FROM appointments;
# ![alt text](<Screenshot 2026-08-04 193434.png>)
SELECT COUNT(*) AS "Completed Appointments" FROM appointments WHERE appointment_status = 'Completed';
# ![alt text](<Screenshot 2026-08-04 200901.png>)

SELECT SUM (consultant_fee) AS "Total Revenue" FROM appointments WHERE appointment_status = 'Completed';
# ![alt text](<Screenshot 2026-08-04 201036.png>)
SELECT AVG(consultant_fee) AS "Average Counsultant fee" FROM appointments ;
# ![alt text](<Screenshot 2026-08-04 195154.png>)
SELECT MAX(consultant_fee) AS "Higest Counsultant fee" FROM appointments ;
# ![alt text](<Screenshot 2026-08-04 195254.png>)
SELECT MIN(consultant_fee) AS "Lowest Counsultant fee" FROM appointments ;
# ![alt text](<Screenshot 2026-08-04 195350.png>)
 SELECT * FROM appointments ORDER BY department  , patient_name; 
# ![alt text](<Screenshot 2026-08-04 195631.png>) 


SELECT department COUNT(*) AS total_appointments FROM appointments GROUP BY department;
# ![alt text](<Screenshot 2026-08-04 200336.png>)
SELECT DISTINCT doctor_name, consultant_fee FROM Appointments WHERE consultant_fee >1000;

SELECT * FROM appointments ORDER BY patient_name ASC LIMIT 5;
# ![alt text](<Screenshot 2026-08-04 200528.png>)
SELECT * FROM appointments WHERE 
appointment_status IN ('Pending', 'Cancelled');
# ![alt text](<Screenshot 2026-08-04 200820.png>)