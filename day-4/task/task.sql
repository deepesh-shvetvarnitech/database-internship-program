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

SELECT patient_name,doctor_name,consultant_fee FROM appointments;
SELECT * FROM appointments WHERE department IN ('Cardiology','Neurology');

SELECT * FROM appointments WHERE patient_name LIKE 'A%';

SELECT * FROM appointments WHERE consultant_fee BETWEEN 700 AND 1300;
SELECT * FROM appointments  ORDER BY consultant_fee   ASC ;
SELECT * FROM appointments  ORDER BY consultant_fee   DESC LIMIT 3;
SELECT COUNT (*) AS "Total Appintments" FROM appointments;
SELECT COUNT(*) AS "Completed Appointments" FROM appointments WHERE appointment_status = 'Completed';

SELECT SUM (consultant_fee) AS "Total Revenue" FROM appointments WHERE appointment_status = 'Completed';
SELECT AVG(consultant_fee) AS "Average Counsultant fee" FROM appointments ;
SELECT MAX(consultant_fee) AS "Higest Counsultant fee" FROM appointments ;
SELECT MIN(consultant_fee) AS "Lowest Counsultant fee" FROM appointments ;
 SELECT * FROM appointments ORDER BY department  , patient_name; 


SELECT department COUNT(*) AS total_appointments FROM appointments GROUP BY department;
SELECT DISTINCT doctor_name, consultant_fee FROM Appointments WHERE consultant_fee >1000;
SELECT * FROM appointments ORDER BY patient_name ASC LIMIT 5;
SELECT * FROM appointments WHERE 
appointment_status IN ('Pending', 'Cancelled');
