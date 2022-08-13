from django.shortcuts import render ,redirect
from django.db import connection
#from ..employee.models import Studentsrom ..employee.forms import StudentsForm



def db(request):
    return render(request, "basic.html")
"""

def loginpage(request):
    if request.method == "POST":
        try:
            login = Students.objects.get(student_email=request.POST['student_email'], student_password=request.POST['student_password'])
            print("student_email", login)
            request.session['student_email'] = login.student_email
            return render(request,'dashboard.html')
        except Students.DoesNotExist as e:
            print('wrong user')
    return render(request,'login.html')
# Create your views here.

def login_s(request):
    if request.method == "POST":
        student_email = request.POST['student_email']
        student_password = request.POST['student_password']
        try:
            cursor = connection.cursor()
            login = cursor.execute("select * from students where student_email= %s and student_password= %s", (student_email , student_password))
            print("student_email", login)
            request.session['student_email'] = login.student_email
        except login.DoesNotExist as e:
            print('wrong user')
    return render(request, 's_login.html')

def logout_s(request):
    try:
        del request.session['student_email']
    except:
        return render(request,'s_login.html')
    return render(request,'s_login.html')
"""
def search(request):
    cursor = connection.cursor()
    cursor.execute("select b.book_name,b.book_edition,b.book_pages,b.book_location,a.author_name,p.publication_name from book as b,author as a, publication as p WHERE b.author_id_id = a.author_id and b.publication_id_id =p.publication_id")
    book = cursor.fetchall()
    return render(request, "search.html", {'book': book})