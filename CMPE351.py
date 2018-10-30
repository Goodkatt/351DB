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
                             autocommit=True,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 
        
        sql = "create database `CMPE351`;"
        sql2 = "use `CMPE351`"
        sql3 = "CREATE TABLE `Student` (`student_id` int(11),`department` varchar(255),`regdate` varchar(255),`regtype` varchar(255),PRIMARY KEY (`student_id`));"
        sql4 = "CREATE TABLE `Submission` (`assignment_id` int(11) AUTO_INCREMENT,`student_id` int(11),`submission_grade` int(11),`sub_deadline` date,`sub_date` date,UNIQUE (`assignment_id`),KEY `FK` (`student_id`));"
        sql5 = "CREATE TABLE `CourseGrade` (`student_id` int(11),`midterm` int(11),`final` int(11),`lab` int(11),KEY `FK` (`student_id`), PRIMARY KEY (`student_id`));"
        cursor.execute(sql)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)
            

finally:
    connection.close()
