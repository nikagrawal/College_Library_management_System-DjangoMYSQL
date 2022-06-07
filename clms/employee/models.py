from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
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
    student_roll = models.IntegerField()
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