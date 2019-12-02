#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

name = form.getvalue('name')
email = form.getvalue('email')

print "Content-type:text/html\r\n\r\n"
print "<HTML>"
print "Registration Form"
print "<table align=absleft datasrc='#xmlRegData' border=2>"
print "<tr>"
print "<td> Name:</td>"
print "<td>%s</span></td>"%(name)
print "</tr>"
print "<tr>"
print "<td>E-mail:</td>"
print "<td>%s</td>"%(email)
print "</tr>"
print "</table>"
print "Is this information correct ?"
print "<form method=GET action=/cgi-bin/confirm.py>"
print "<input type=radio name='confirm' value='yes'> YES"  
print "<input type=radio name='confirm' value='no' checked> NO" 
print "<input type=submit value=Submit>"     
print "<input type=reset value=Reset>"
print "</form>"
print "</HTML>"