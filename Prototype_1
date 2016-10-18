from django.shortcuts import render
from django.http import HttpResponse

import MySQLdb
import sys
import signup

def insert_user(uname, pwrd):
    query = "INSERT INTO user(Username,Password) " \
            "VALUES(%s,%s)"
    args = (uname, pwrd)
    cursor.execute(query, args)
    query = "INSERT INTO userdetails(Username,Fname,Lname,Nickname,Techlevel,Years,Rating,Bio) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    l="NULL"
    args = (uname,l,l,l,l,l,l,l)
    cursor.execute(query, args)
    connection.commit()


def update_user(uname,fn,ln,nn,tl,yrs,rtg,bio):
    query = "UPDATE userdetails set Fname = %s, Lname = %s ,Nickname = %s,Techlevel = %s,Years = %s,Rating = %s,Bio = %s where Username = %s" 
    args = (fn,ln,nn,tl,yrs,rtg,bio,uname)
    cursor.execute(query, args)
    connection.commit()

def update_skills(uname,skl,gnr):
	query = "INSERT INTO skills(Username,Instrument,genre) " \
            "VALUES(%s,%s,%s)" 
	args = (uname,skl,gnr)
	cursor.execute(query, args)
	connection.commit()


# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "localhost", user = "root", passwd = "rohit", db = "jamming")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

#insert_user("hello1","world")
#update_user("hello1","a","b","c","d","e","f","g")
#update_skills("hello1","sd","asc")


# execute the SQL query using execute() method.
cursor.execute ("select * from user")
# fetch all of the rows from the query
data = cursor.fetchall ()
# print the rows
# close the cursor object
cursor.close ()
# close the connection
connection.close ()
def index(request):
    return HttpResponse(data)
