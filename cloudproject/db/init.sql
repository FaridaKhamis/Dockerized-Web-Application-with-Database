SET sql_notes = 1;  -- Enable notice output

--creates a new database called studentdb if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS studentdb;

--selects the studentdb database, making it the active database for subsequent queries.
USE studentdb;

--drops the table named students if it exists and 
--this ensures that any previous version of the table is removed before creating a new one.
DROP TABLE IF EXISTS students;

--we created the students table
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    cgpa DECIMAL(3,2),
    additional_info TEXT
);

--here are the data displayed in the table
INSERT INTO students (id, name, age, cgpa, additional_info) VALUES
(2202125,'Malak Ahmed', 19, 3.80, NULL),
(2202136,'Farida Khamis', 20, 3.90, NULL),
(220591,'Malak Mohamed', 19, 3.90, NULL),
(220594,'Nadeen Ahmed', 19, 3.90, NULL),
(2203171,'Jana Nabil', 19, 3.80, NULL);

-- After inserting, check the contents of the table
SELECT * FROM students;

-- Then perform the update
UPDATE students
SET additional_info = 'Undergraduate Level 2'
WHERE age IN (19, 20);

-- Check if the update was successful
SELECT * FROM students;