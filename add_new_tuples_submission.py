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
    with connection.cursor() as cursor, open('all_tue.csv', newline='') as csvfile, open('all_thu.csv', newline='') as csvfiletwo:
        # 
        reader = csv.DictReader(csvfile, delimiter=';')
        readertwo = csv.DictReader(csvfiletwo, delimiter=';')
        sql = "INSERT INTO `Submission` (`student_id`)VALUES (%s);"
        for row in reader:
            cursor.execute(sql, (row['StudentID']))
        for row in readertwo:
            cursor.execute(sql, (row['StudentID']))
            
        result = cursor.fetchall()

finally:
    connection.close()
