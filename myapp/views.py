from distutils.command.build_scripts import first_line_re
from email import message
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse 
import mysql.connector as sql 
from myapp.models import books
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"myapp/index.html")
def main(request):
    return render(request,"myapp/main.html")
firstname=''
lastname=''
email=''
passw=''

Book_id =''
Book_name=''
Aisle_number=''
def signup(request):
    global firstname,lastname,email,passw
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",password="sakshi0912",database="library")
        cursor=m.cursor()
        d=request.POST
        for  key,value in d.items():
            if key=="firstname":
                firstname=value
            if key=="lastname":
                lastname=value
            if key== "email":
                email=value
            if key=="passw":
                passw=value
     
        c="insert into user values('{}','{}','{}','{}')".format(firstname,lastname,email,passw)
        cursor.execute(c)
        m.commit()

    return render(request,"myapp/signup.html")

def login(request):
    global email,passw
    if request.method == "POST":
         m=sql.connect(host="localhost",user="root",password="sakshi0912",database="library")
         cursor=m.cursor()
         d=request.POST
         for  key,value in d.items():
            if key=="firstname":
             firstname=value
            if key=="lastname":
              lastname=value
            if key== "email":
              email=value
            if key=="passw":
             passw=value
         c="select * from user where email='{}' and passw='{}'".format(email,passw)
         cursor.execute(c)
         t=tuple(cursor.fetchall())
         if t==():
            return render(request,'myapp/error.html')
         else:
            return render(request,'myapp/main.html')


    return render(request,"myapp/login.html")

def logout(request):
    pass
def addbook(request):
    global Book_id,Book_name,Aisle_number
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",password="sakshi0912",database="library")
        cursor=m.cursor()
        d=request.POST
        for  key,value in d.items():
            if key=="Book_id":
                Book_id=value
            if key=="Book_name":
                Book_name=value
            if key== "Aisle_number":
                Aisle_number=value
         
     
        c="insert into books values('{}','{}','{}')".format(Book_id,Book_name,Aisle_number)
        cursor.execute(c)
        m.commit()

    return render(request,"myapp/addbook.html")


def showbook(request):
    resultsdisplay=books.objects.all()
    return render(request,"myapp/showbooks.html",{'books':resultsdisplay})

def delete(request,id):
    usr=books.objects.get(id=id)
    usr.delete()
    message.info(request,"item")
    return redirect(request,"/showbooks")

    
    
    

