#This script connects to mysql server with given connection parameters. 
#Modify the user, password and database information to adapt to your environment. 
#Before running, make sure that you activated the cmpe351 virtual environment and installed pymysql within the environment. 

import pymysql.cursors #import cursors module of pymysql package
import csv
a=[]
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Montezumo0',
                             db='CMPE351',
                             autocommit=True,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor, open('all_thu.csv', newline='') as csvfile, open('all_tue.csv', newline='') as csvfiletwo:
        # 
        reader = csv.DictReader(csvfile, delimiter=';')
        readertwo = csv.DictReader(csvfiletwo, delimiter=';')
        sql = "INSERT INTO `Student` (`student_id`, `department`, `regdate`, `regtype`)VALUES (%s, %s, %s, %s);"
        sqltwo = "INSERT INTO `CourseGrade`(`student_id`) VALUES (%s)"
        sqlten = "INSERT INTO `Submission`(`student_id`) VALUES (%s)"
        sqlthree = "UPDATE `CourseGrade` SET `lab` = FLOOR(0 + RAND() * 100);"
        sqlfour = "UPDATE `CourseGrade` SET `midterm` = FLOOR(0 + RAND() * 100);"
        sqlfive = "UPDATE `CourseGrade` SET `final` = FLOOR(0 + RAND() * 100);"
        sqlsix = "ALTER TABLE `CourseGrade` ADD `quiz` int(11);"
        sqlseven = "UPDATE `CourseGrade` SET `quiz` = FLOOR(0 + RAND() * 100);"
        sqleight = "ALTER TABLE `CourseGrade` ADD `overall` int(11);"
        sqlnine = "UPDATE `CourseGrade` inner join `Student` on `CourseGrade`.`student_id`=`Student`.`student_id` set `CourseGrade`.`overall`=floor(((`CourseGrade`.`midterm`*25)+(`CourseGrade`.`quiz`*15)+(`CourseGrade`.`lab`*20)+(`CourseGrade`.`final`*40))/100);"
        sqleleven = "ALTER TABLE `Submission` ADD `bonus` int(11);"
        sqltwelve = "UPDATE `Submission` SET `bonus` = 10;"
        sqlthirteen = "UPDATE `Submission` SET `sub_deadline` = '2017-12-01';"

        cursor.execute(sqlsix)
        cursor.execute(sqleight)
        cursor.execute(sqleleven)
        for row in reader:
            cursor.execute(sql, (row['StudentID'], row['Department'], row['Reg.Date'], row['Reg.Type']))
            cursor.execute(sqltwo, (row['StudentID']))
            cursor.execute(sqlten, (row['StudentID']))
            cursor.execute(sqlthree)
            cursor.execute(sqlfour)
            cursor.execute(sqlfive)
            cursor.execute(sqlseven)
            cursor.execute(sqlnine)
            cursor.execute(sqltwelve)
            cursor.execute(sqlthirteen)
        for row in readertwo:
            cursor.execute(sql, (row['StudentID'], row['Department'], row['Reg.Date'], row['Reg.Type']))
            cursor.execute(sqltwo, (row['StudentID']))
            cursor.execute(sqlten, (row['StudentID']))
            cursor.execute(sqlthree)
            cursor.execute(sqlfour)
            cursor.execute(sqlfive)
            cursor.execute(sqlseven)
            cursor.execute(sqlnine)
            cursor.execute(sqltwelve)
            cursor.execute(sqlthirteen)

        result = cursor.fetchall()

finally:
    connection.close()
