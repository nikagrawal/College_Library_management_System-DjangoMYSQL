from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    epassword = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)

    class Meta:
        db_table = "author"


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)

    class Meta:
        db_table = "department"

class Publication(models.Model):
    publication_id = models.AutoField(primary_key=True)
    publication_name = models.CharField(max_length=100)

    class Meta:
        db_table = "publication"



class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_roll = models.IntegerField(unique=True)
    student_first_name = models.CharField(max_length=100)
    student_last_name = models.CharField(max_length=100)
    student_address = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    student_mob_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    student_email = models.EmailField(max_length=254)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    student_sem = models.IntegerField()
    student_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_dob = models.DateField()
    student_password = models.CharField(max_length=50)
    department =models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = "students"

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    book_class_no = models.CharField(max_length=30, unique=True)
    publication_id = models.ForeignKey(Publication, on_delete=models.CASCADE)
    book_edition = models.DateField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    received_by = models.CharField(max_length=200)
    book_bill_date = models.DateField()
    book_bill_no = models.IntegerField()
    book_pages = models.IntegerField()
    book_price = models.IntegerField()
    book_date_of_entry = models.DateField()
    book_location = models.CharField(max_length=20)
    class Meta:
        db_table = "book"

class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    class Meta:
        db_table = "issue"

class Return(models.Model):
    return_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    panalty = (
        ('y', 'yes'),
        ('n', 'no'),
    )
    panalty_status = models.CharField(max_length=1, choices=panalty)

    class Meta:
        db_table = "return_b"

class Penalty(models.Model):
    penalty_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    penalty_amount = models.IntegerField()
    penalty_pay = models.IntegerField()
    class Meta:
        db_table = "penalty"

class Book_lost(models.Model):
    book_lost_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()
    class Meta:
        db_table = "book_lost"

class Demand(models.Model):
    demand_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField()
    class Meta:
        db_table = "demand"





