UPDATE Submission SET sub_date = CURRENT_TIMESTAMP - INTERVAL FLOOR(RAND() * 14) DAY WHERE sub_date IS NULL;

UPDATE Submission SET bonus = 10 WHERE bonus IS NULL;

UPDATE Submission SET sub_deadline = '2017-12-01' WHERE sub_deadline IS NULL;

UPDATE Submission SET submission_grade = 10 WHERE sub_deadline > sub_date;
