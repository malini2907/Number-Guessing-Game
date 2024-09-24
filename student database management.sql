CREATE TABLE Students (
    student_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    date_of_birth DATE,
    email VARCHAR2(100) UNIQUE
);

CREATE TABLE Courses (
    course_id NUMBER PRIMARY KEY,
    course_name VARCHAR2(100),
    instructor_name VARCHAR2(100)
);


CREATE TABLE Enrollments (
    enrollment_id NUMBER PRIMARY KEY,
    student_id NUMBER,
    course_id NUMBER,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);


-- Insert Students
INSERT INTO Students VALUES (1, 'John', 'Doe', TO_DATE('1995-01-01', 'YYYY-MM-DD'), 'john.doe@example.com');
INSERT INTO Students VALUES (2, 'Jane', 'Smith', TO_DATE('1996-02-02', 'YYYY-MM-DD'), 'jane.smith@example.com');

-- Insert Courses
INSERT INTO Courses VALUES (1, 'Introduction to SQL', 'Dr. Alice Johnson');
INSERT INTO Courses VALUES (2, 'Data Structures', 'Prof. Bob Smith');

-- Insert Enrollments
INSERT INTO Enrollments VALUES (1, 1, 1, TO_DATE('2024-01-10', 'YYYY-MM-DD')); -- John Doe in SQL
INSERT INTO Enrollments VALUES (2, 2, 2, TO_DATE('2024-01-12', 'YYYY-MM-DD')); -- Jane Smith in Data Structures


SELECT * FROM Students;


SELECT * FROM Courses;


-- Get students enrolled in a specific course
SELECT s.first_name, s.last_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 1;  -- Course ID for 'Introduction to SQL'

-- Update a student's email
UPDATE Students
SET email = 'john.newemail@example.com'
WHERE student_id = 1;


-- Delete an enrollment record
DELETE FROM Enrollments
WHERE enrollment_id = 1;  -- ID of the enrollment to delete

COMMIT;
