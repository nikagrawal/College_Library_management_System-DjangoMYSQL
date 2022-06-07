from django.shortcuts import render, redirect
from .forms import EmployeeForm, AuthorForm, DepartmentForm, PublicationForm, StudentsForm
from .models import Employee, Author, Department, Publication, Students
# Create your views here.
def base(request):
    return render(request, "dashboard.html")

def dash(request):
    return render(request, "dashboard.html")
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
    publication = Publication  .objects.get(publication_id=publication_id)
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
Student  add / update / display/delete
"""
def Students_show(request):
    student = Students.objects.all()
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
        'department' : department,
        'form': form})

def Students_destroy(request, student_id):
    student = Students.objects.get(student_id=student_id)
    student.delete()
    return redirect("/Students_show")


"""
Publication  add / update / display/ delete
"""




