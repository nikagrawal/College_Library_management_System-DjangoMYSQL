# Django Clms (Create College management system) 

This project contains-
 - creating table using ORM
 - listing, fetching, editing and deleting data from and to database

# For step by step guide open file- stepBystep.docs

System need to install- Python and python virtual environment

a. Download and Install python

b. Create virtual environment(pip should be installed(check version- pip --version))
Install either virtualenvwrapper or virtualenv(for more info goto- link)
install virtual environment- pip install virtualenv
Create virtual environment- virtualenv <virtual-env>
Now activate virtual env - cd <virtual-env>/Scripts/activate

c. Install Django using command -
pip install django
Check django version command-
	python -m django --version


To create a Django System-application that performs CRUD operations, follow the following steps.
1. Create a Project, using command- 
$ django-admin startproject crudexample  
2. Create an App, using command- 
$ python3 manage.py startapp employee  

3. Database Setup -
Create a database djangodb in mysql, and configure into the settings.py file of django project. See the example.
// settings.py
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'djangodb',  
        'USER':'root',  
        'PASSWORD':'mysql',  
        'HOST':'localhost',  
        'PORT':'3306'  
    }  
}  

