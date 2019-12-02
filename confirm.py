#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import pymysql

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

confirm = form.getvalue('confirm')
name="Jack"
email="jack@gmail.com"
print "Content-type:text/html\r\n\r\n"

if confirm == 'no':
    print "<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >"
    print "<TR VALIGN=TOP>"
    print "<TD>"
    print "<pre>"
    print "So, The Information Is Incorrect."
    print "<a href='/cgi-bin/regist.py'>Please Registration Again</a>"
    print "<a href='regist.html'>Back To Top</a>"
    print "</pre>"
    print "</TD>"
    print "</TR>"
    print "</TABLE>"
else:
    print "<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >"
    print "<TR VALIGN=TOP>"
    print "<TD>"
    print "<pre>"
    print "Registration Successful"

    print "     Thanks"
    print "</pre>"
    print "</TD>"
    print "</TR>"
    print "</TABLE>"

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

