'''
Created on Mar 26, 2020
This is the in-class demo of connecting to a database
@author: jakeluebbe
'''
# Connecting to SQL Server with Python
# Install the pyodbc library first:
# pip install pyodbc
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import sys
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=il-server-001.uccc.uc.edu\mssqlserver2012;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

#Above is the connection string to our database. This was provided b/c it's a pain in the butt and cannot figure out otherwise
cursor = conn.cursor() 
cursor.execute('SELECT * FROM tAmericanAthleticConference')    # Submit a query to the SQL Server instance and store the results in the cursor object

total_enrollment = 0
# Step through all the rows in the results set from the cursor object
for row in cursor:
    print(row);     # All columns in the row
    print (row[1]); # Second column
    print (row[2]); # Third column
    print (row[3]); # Fourth column
    total_enrollment = total_enrollment + int(row[2])   # running sum of enrollments
    

print ("Total enrollment = " + str(total_enrollment))
