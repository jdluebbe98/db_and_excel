'''
Created on Mar 31, 2020

@author: jakeluebbe
'''

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=il-server-001.uccc.uc.edu\mssqlserver2012;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')


cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')
#for row in cursor:
#    print(row.University)

# The column names are case sensitive!
universities = [myRow.University.strip() for myRow in cursor.fetchall()]
print (universities)

# Need to re-read the data
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')    # Submit a query to the SQL Server instance and store the results in the cursor object
totalEnrollment = sum([int(myRow.Enrollment) for myRow in cursor.fetchall()])
print (totalEnrollment)
