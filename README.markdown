# Project

## Table of Contents

* Create Database
* Fill Database
* Make Changes on Tables

### Steps:

* Please use the **all_thu.csv** and **all_tue.csv** files to read, other CSV files gives errors about spacing in column names.

* Change directory of CSV files if needed.

* Design python files according to your MySQL username and password.

*  Execute **CMPE351.py** to create database, then execute **fill_database.py**
  to fill the tables and to update tables or to insert new attributes into tables which is asked in **project.pdf**

*  **fill_database.py** fills the all attributes in database except **submission_grade** and **sub_date** we will use **queries.sql** to fill these attributes.

*   After executing the **queries.sql** database will be ready to use with all the tables filled. In the **Student** table there are 86 records according to CSV' s. Same as in **CourseGrade** and **Submission** table.

*   We can add more tuples into **Submission** table by executing **add_new_tuples_submission.py** which adds tuesday students again into the table.


*  But the problem here is **submission_grade**, **sub_deadline**, **sub_date** and **bonus** attributes are NULL for each of every new tuple. Which means students has an **assignment_id** but student didn't make any submissions.

* To fix the problem for new tuples we need to execute queries written below or you can just **source** the **queries.sql** in MySQL command prompt:

```
UPDATE Submission SET bonus = 10 WHERE bonus IS NULL;
UPDATE Submission SET sub_deadline = '2017-12-01' WHERE sub_deadline IS NULL;
UPDATE Submission SET sub_date = CURRENT_TIMESTAMP - INTERVAL FLOOR(RAND() * 14) DAY WHERE sub_date IS NULL;
UPDATE Submission SET submission_grade = 10 WHERE sub_deadline > sub_date AND submission_grade IS NULL;


```

By doing this we confirm that one student can make one or more Submissions.

## Queries for Joining Tables:

```
SELECT Student.student_id, CourseGrade.midterm, CourseGrade.quiz, CourseGrade.final, CourseGrade.lab
FROM Student
INNER JOIN CourseGrade ON Student.student_id=CourseGrade.student_id;


SELECT Student.student_id, Submission.sub_date, Submission.submission_grade
FROM Student
INNER JOIN Submission ON Student.student_id=Submission.student_id;


SELECT *
FROM Student
 JOIN CourseGrade ON Student.student_id=CourseGrade.student_id
 JOIN Submission ON Student.student_id=Submission.student_id;

```

## Screenshots:

### Midterm, Lab, Final grades of Students

[![midterm_final_lab.png](https://s18.postimg.org/il14m7j49/midterm_final_lab.png)](https://postimg.org/image/5tmyfp9c5/)

### Students ordered according to their midterm grades

[![sort_midterm.png](https://s18.postimg.org/jajwynjop/sort_midterm.png)](https://postimg.org/image/hvic9xilh/)

## Notes:
None of the tables violates any normalization forms as far as i have seen
