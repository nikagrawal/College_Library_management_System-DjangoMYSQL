from django.shortcuts import render, redirect
from django.db import connection
from .forms import EmployeeForm, AuthorForm, DepartmentForm, PublicationForm, StudentsForm, BookForm, IssueForm, ReturnForm, PenaltyForm ,Book_lostForm ,DemandForm
from .models import Employee, Author, Department, Publication, Students, Book, Issue ,Return ,Penalty ,Book_lost ,Demand
# Create your views here.
def loginpage(request):
    if request.method == "POST":
        try:
            login = Employee.objects.get(eemail=request.POST['eemail'], epassword=request.POST['epassword'])
            print("eemail", login)
            request.session['eemail'] = login.eemail
            return render(request,'dashboard.html')
        except Employee.DoesNotExist as e:
            print('wrong user')
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['eemail']
    except:
        return render(request,'login.html')
    return render(request,'login.html')

def base(request):
    cursor = connection.cursor()
    std="SELECT COUNT(student_id) FROM students"
    cursor.execute(std)
    student_dash = cursor.fetchall()
    aut = "SELECT COUNT(author_id) FROM author"
    cursor.execute(aut)
    auth = cursor.fetchall()
    pub = "SELECT COUNT(publication_id) FROM publication"
    cursor.execute(pub)
    publi = cursor.fetchall()
    bok = "SELECT COUNT(book_id) FROM Book"
    cursor.execute(bok)
    booki = cursor.fetchall()

    return render(request, "dashboard.html", {'student_dash': student_dash,
                                              'auth': auth,
                                              'publi':publi,
                                              'booki': booki
                                              })


def dash(request):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    student_dash = cursor.fetchall()
    return render(request, "dashboard.html", {'student_dash': student_dash})
"""

employee  add / update / display/delete
"""

def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})



def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
"""

employee  add / update / display/ delete
"""

"""

Author  add / update / display/delete
"""

def Author_show(request):
    authors = Author.objects.all()
    return render(request, "Author_display.html", {'authors': authors})


def author_a(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Author_show')
            except:
                pass
    else:
        form = AuthorForm()
    return render(request, 'Author.html', {'form': form})



def Author_edit(request, author_id):
    author = Author.objects.get(author_id=author_id)
    return render(request, 'Author_update.html', {'author': author})


def Author_update(request, author_id):
    author = Author.objects.get(author_id=author_id)
    form = AuthorForm(request.POST, instance = author)
    if form.is_valid():
        form.save()
        return redirect("/Author_show")
    return render(request, 'Author_update.html', {'author': author})


def Author_destroy(request,author_id):
    author = Author.objects.get(author_id=author_id)
    author.delete()
    return redirect("/Author_show")
"""
Author  add / update / display/ delete
"""

"""
departments  add / update / display/delete
"""

def Department_show(request):
    departments = Department.objects.all()
    return render(request, "Department_display.html", {'departments': departments})


def department_a(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Department_show')
            except:
                pass
    else:
        form = DepartmentForm()
    return render(request, 'Department.html', {'form': form})



def Department_edit(request, department_id):
    department = Department.objects.get(department_id=department_id)
    return render(request, 'Department_update.html', {'department': department})


def Department_update(request, department_id):
    department = Department.objects.get(department_id=department_id)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        return redirect("/Department_show")
    return render(request, 'Department_update.html', {'department': department})


def Department_destroy(request, department_id):
    department = Department.objects.get(department_id=department_id)
    department.delete()
    return redirect("/Department_show")
"""

departments  add / update / display/ delete
"""

"""
Publication  add / update / display/delete
"""

def Publication_show(request):
    publications = Publication.objects.all()
    return render(request, "Publication_display.html", {'publications': publications})


def publication_a(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Publication_show')
            except:
                  pass
    else:
        form = PublicationForm()
    return render(request, 'Publication.html', {'form': form})



def Publication_edit(request, publication_id):
    publication = Publication.objects.get(publication_id=publication_id)
    return render(request, 'Publication_update.html', {'publication': publication})


def Publication_update(request, publication_id):
    publication = Publication.objects.get(publication_id=publication_id)
    form = PublicationForm(request.POST, instance=publication)
    if form.is_valid():
        form.save()
        return redirect("/Publication_show")
    return render(request, 'Publication_update.html', {'publication': publication})


def Publication_destroy(request, publication_id):
    publication = Publication.objects.get(publicationid=publication_id)
    publication.delete()
    return redirect("/Publication_show")

"""
Publication  add / update / display/ delete
"""

"""
book  add / update / display/delete
"""
def Students_show(request):
    cursor = connection.cursor()
    cursor.execute("select s.student_id,s.student_roll,s.student_first_name,s.student_last_name,s.student_address,s.student_mob_no,s.student_email,s.student_sem,s.student_gender,s.student_dob,s.student_password,d.department_name from students as s,department as d where s.department_id = d.department_id")
    student = cursor.fetchall()
    return render(request, "Students_display.html", {'student': student})

def students_a(request):
    department = Department.objects.all()
    if request.method == "POST":

        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Students_show')
            except:
                pass
    else:
        form = StudentsForm()
    return render(request, 'Students.html', {
        'department': department,
        'form': form})

def Students_edit(request, student_id):
    department = Department.objects.all()
    student = Students.objects.get(student_id=student_id)
    return render(request, 'Students_update.html', {
        'department': department,
        'student': student,
        })


def Students_update(request, student_id):
    department = Department.objects.all()
    Student = Students.objects.get(student_id=student_id)
    form = StudentsForm(request.POST, instance=Student)

    if form.is_valid():
        form.save()
        return redirect("/Students_show")
    return render(request, 'Students_update.html', {
        'department': department,
        'Student': Student,
        })


def Students_destroy(request, student_id):
    student = Students.objects.get(student_id=student_id)
    student.delete()
    return redirect("/Students_show")


"""
Student  add / update / display/ delete
"""


"""
Book  add / update / display/delete
"""
def Book_show(request):
    cursor = connection.cursor()
    cursor.execute("select b.book_id,b.book_name,b.book_class_no,b.book_edition,b.received_by,b.book_bill_date,b.book_bill_no,b.book_pages,b.book_price,b.book_date_of_entry,b.book_location,a.author_name,p.publication_name from book as b,author as a, publication as p WHERE b.author_id_id = a.author_id and b.publication_id_id =p.publication_id")
    book = cursor.fetchall()
    return render(request, "Book_display.html", {'book': book})

def book_a(request):
    author = Author.objects.all()
    publications = Publication.objects.all()
    if request.method == "POST":

        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Book_show')
            except:
                pass
    else:
        form = BookForm()
    return render(request, 'Book.html', {
        'author': author,
        'publications': publications,
        'form': form})

def Book_edit(request, book_id):
    book = Book.objects.get(book_id=book_id)


    return render(request, 'Book_update.html', {

        'book': book})


def Book_update(request, book_id):
    book = Book.objects.get(book_id=book_id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect("/Book_show")
    return render(request, 'Book_update.html', {

        'book': book})


def Book_destroy(request, book_id):
    book = Book.objects.get(book_id=book_id)
    book.delete()
    return redirect("/Book_show")


"""
book  add / update / display/ delete
"""

"""
Issue  add / update / display/delete
"""
def Issue_show(request):
    cursor = connection.cursor()
    cursor.execute("SELECT i.issue_id, p.publication_name,s.student_roll,s.student_first_name,b.book_name,i.return_date,i.issue_date FROM publication as p, students as s, book as b,issue as i WHERE i.publication_id=p.publication_id and i.student_id= s.student_id AND  i.book_id= b.book_id")
    issue = cursor.fetchall()
    return render(request, "Issue_display.html", {'issue': issue})

def issue_a(request):
    student = Students.objects.all()
    publications = Publication.objects.all()
    book = Book.objects.all()
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Issue_show')
            except:
                pass
    else:
        form = IssueForm()
    return render(request, 'Issue.html', {
        'student': student,
        'book': book,
        'publications': publications,
        'form': form})

def Issue_edit(request, issue_id):
    issue = Issue.objects.get(issue_id=issue_id)


    return render(request, 'Issue_update.html', {

        'issue': issue})


def Issue_update(request, issue_id):
    issue = Issue.objects.get(issue_id=issue_id)
    form = IssueForm(request.POST, instance=issue)
    if form.is_valid():
        form.save()
        return redirect("/Issue_show")
    return render(request, 'Issue_update.html', {

        'issue': issue})


def Issue_destroy(request, issue_id):
    issue = Issue.objects.get(issue_id=issue_id)
    issue.delete()
    return redirect("/Book_show")


"""
Issue  add / update / display/ delete
"""

"""
Return  add / update / display/delete
"""
def Return_show(request):
    cursor = connection.cursor()
    cursor.execute("SELECT i.return_id, p.publication_name,s.student_roll,s.student_first_name,b.book_name,i.return_date,i.issue_date, i.panalty_status FROM publication as p, students as s, book as b,return_b as i WHERE i.publication_id=p.publication_id and i.student_id= s.student_id AND  i.book_id= b.book_id")
    book_retun = cursor.fetchall()
    return render(request, "Return_display.html", {'book_retun': book_retun})

def return_a(request):
    student = Students.objects.all()
    publications = Publication.objects.all()
    book = Book.objects.all()
    if request.method == "POST":
        form = ReturnForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Return_show')
            except:
                pass
    else:
        form = IssueForm()
    return render(request, 'Return.html', {
        'student': student,
        'book': book,
        'publications': publications,
        'form': form})

def Return_edit(request, return_id):
    book_return = Return.objects.get(return_id=return_id)


    return render(request, 'Return_update.html', {

        'book_return': book_return})


def Return_update(request, return_id):
    book_return = Return.objects.get(return_id=return_id)
    form = ReturnForm(request.POST, instance=book_return)
    if form.is_valid():
        form.save()
        return redirect("/Return_show")
    return render(request, 'Return_update.html', {

        'book_return': book_return})


def Return_destroy(request, return_id):
    book_return = Return.objects.get(return_id=return_id)
    book_return.delete()
    return redirect("/Return_show")

"""
Return  add / update / display/ delete
"""


"""
penalty  add / update / display/delete
"""
def Penalty_show(request):
    cursor = connection.cursor()
    cursor.execute("SELECT i.penalty_id,s.student_roll,s.student_first_name,b.book_name,i.penalty_amount,i.penalty_pay FROM students as s, book as b,penalty as i WHERE i.student_id= s.student_id AND i.book_id= b.book_id")
    penalty = cursor.fetchall()
    return render(request, "Penalty_show.html", {'penalty': penalty})

def penalty_a(request):
    student = Students.objects.all()
    book = Book.objects.all()
    if request.method == "POST":
        form = PenaltyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Penalty_show')
            except:
                pass
    else:
        form = PenaltyForm()
    return render(request, 'Penalty.html', {
        'student': student,
        'book': book,
        'form': form})

def Penalty_edit(request, penalty_id):
    penalty = Penalty.objects.get(penalty_id=penalty_id)


    return render(request, 'Penalty_update.html', {

        'penalty': penalty})


def Penalty_update(request, penalty_id):
    penalty = Penalty.objects.get(penalty_id=penalty_id)
    form = PenaltyForm(request.POST, instance=penalty )
    if form.is_valid():
        form.save()
        return redirect("/Penalty_show")
    return render(request, 'Penalty_update.html', {

        'penalty': penalty})


def Penalty_destroy(request, return_id):
    penalty = Penalty.objects.get(return_id=return_id)
    penalty.delete()
    return redirect("/Penalty_show")

"""
penalty   add / update / display/ delete
"""

"""
Book_lost  add / update / display/delete
"""
def Book_lost_show(request):
    cursor = connection.cursor()
    cursor.execute("SELECT i.Book_lost_id,s.student_roll,s.student_first_name,b.book_name,i.amount FROM students as s, book as b,Book_lost as i WHERE i.student_id= s.student_id AND i.book_id= b.book_id")
    book_lost = cursor.fetchall()
    return render(request, "Book_lost_display.html", {'book_lost': book_lost})

def book_lost_a(request):
    student = Students.objects.all()
    book = Book.objects.all()
    if request.method == "POST":
        form = Book_lostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Book_lost_show')
            except:
                pass
    else:
        form = Book_lostForm()
    return render(request, 'Book_lost.html', {
        'student': student,
        'book': book,
        'form': form})

def Book_lost_edit(request, book_lost_id):
    book_lost = Book_lost.objects.get(book_lost_id=book_lost_id)
    return render(request, 'Book_lost_update.html', {'book_lost': book_lost})


def Book_lost_update(request, book_lost_id):
    book_lost = Book_lost.objects.get(book_lost_id=book_lost_id)
    form = Book_lostForm(request.POST, instance=book_lost )
    if form.is_valid():
        form.save()
        return redirect("/Book_lost_show")
    return render(request, 'Book_lost_update.html', {

        'book_lost': book_lost})


def Book_lost_destroy(request, book_lost_id):
    book_lost = Book_lost.objects.get(book_lost_id=book_lost_id)
    book_lost.delete()
    return redirect("/Book_lost_show")

"""
Book_lost   add / update / display/ delete
"""
"""
Demand  add / update / display/delete
"""
def Demand_show(request):
    cursor = connection.cursor()
    cursor.execute("SELECT i.demand_id,b.book_name,b.book_edition,i.date FROM students as s, book as b,demand as i WHERE  i.book_id= b.book_id")
    demand = cursor.fetchall()
    return render(request, "Demand_display.html", {'demand': demand})

def demand_a(request):
    student = Students.objects.all()
    book = Book.objects.all()
    if request.method == "POST":
        form = DemandForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Demand_show')
            except:
                pass
    else:
        form = DemandForm()
    return render(request, 'Demand.html', {
        'student': student,
        'book': book,
        'form': form})

def Demand_edit(request, demand_id):
    demand = Demand.objects.get(demand_id=demand_id)


    return render(request, 'Demand_update.html', {

        'demand': demand})


def Demand_update(request, demand_id):
    demand = Demand.objects.get(demand_id=demand_id)
    form = DemandForm(request.POST, instance=demand )
    if form.is_valid():
        form.save()
        return redirect("/Demand_show")
    return render(request, 'Demand_update.html', {

        'demand': demand})


def Demand_destroy(request, demand_id):
    demand = Demand.objects.get(demand_id=demand_id)
    demand.delete()
    return redirect("/Demand_show")

"""
Demand   add / update / display/ delete
"""











