from django import forms
from .models import Employee
from .models import Author
from .models import Department
from .models import Publication
from .models import Students

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
