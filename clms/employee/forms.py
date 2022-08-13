from django import forms
from .models import Employee
from .models import Author
from .models import Department
from .models import Publication
from .models import Students
from .models import Book
from .models import Issue
from .models import Return
from .models import Penalty
from .models import Book_lost
from .models import Demand


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['publication_name']


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_roll', 'student_first_name', 'student_last_name', 'student_address','student_sem', 'student_mob_no', 'student_email', 'student_gender', 'student_dob', 'student_password', 'department']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name','book_class_no','publication_id','book_edition','author_id','received_by','book_bill_date','book_bill_no','book_pages','book_price','book_date_of_entry','book_location']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['student','book','publication','issue_date','return_date']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['student','book','publication','issue_date','return_date','panalty_status']

class PenaltyForm(forms.ModelForm):
    class Meta:
        model = Penalty
        fields = ['student', 'book','penalty_amount','penalty_pay']

class Book_lostForm(forms.ModelForm):
    class Meta:
        model = Book_lost
        fields = ['student', 'book','amount']

class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ['student', 'book','date']

