#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","cs531" )

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM regist\
       WHERE EMAIL> '%s'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      name = row[0]
      email = row[1]
      print ("name = %s,email = %s" % \
             (NAME,EMAIL))
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()
