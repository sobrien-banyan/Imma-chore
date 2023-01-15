# Imm-a-chore

### Stack: Python3, HTML, CSS, Django, Bootstrap

## Developers:
The Ingenious, Insightful and Outstanding: Amanda Testerman, Sean O'Brien, and Christopher Cialone

## Description:
The Imma-chore App is a practical and fun way for Parents and Children to work together to learn how to delegate and receive chores, appreciate the value of earning your own money and finally, teaching the kids about responsibility and the virtue of accountability.

### The HomePage
New Parents to the application will enter their name and then click on the 'Create' button


## To start building the project:

### 1. Create a virtual environment

At the root folder of the repository run:
```
python3 -m venv venv
```
Make sure to call your virtual environment "venv"

### 2. Run virtual environment
#### On Windows:
Windows Powershell users:
```
venv\Scripts\activate.bat
```
Bash users:
```
source venv/Scripts/activate
```
#### On Unix or MacOS:
```
source venv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. install django and migrate
`pip install django` , `python manage.py migrate`

### 4. Run Django
```
python manage.py runserver
```

And go to `http://localhost:8000` or `http://127.0.0.1:8000/`


## Summary

1. Clone the repo to your computer
2. run `source venv/bin/activate` 
3. run `pip install -r requirements.txt`
4. run `python manage.py migrate`
5. run `python manage.py runserver`



## steps taken to create this
1. Create virtual environment  ->      ‘python3 -m venv venv’
2. Activate it  ->   source venv/bin/activate
3. Install Django ‘pip install django’
4. Create a django project with ‘Django-admin startproject <project_name>’
5. ‘pip3 freeze > requirements.txt’
6. Run ‘python3 manage.py runserver’
7. Create an ‘app’ inside your project with ‘python3 manage.py startapp <app_name>’
8. Install your new app in your projects setting file


### In imma_chore_server/settings add:
```
INSTALLED_APPS = [
    'imma_chore_app.apps.ImmaChoreAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### In imma_chore_server/urls.py add:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imma_chore_app.urls')),
]
```

### In imma_chore_app create a file called urls.py and add:
```
from django.urls import path

from imma_chore_app.views import HomeView, ParentView, KidView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('parent/<int:parent_id>/<int:kid_id>/<int:chore_id>', ParentView.as_view(), name='parent'),
    path('kid/<int:kid_id>/<int:chore_id>', KidView.as_view(), name='kid'),
    
]
```


create model

```
from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class Chore(models.Model):
    name = models.CharField(max_length=35)
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null=True)
    description = models.CharField(max_length=35)
    payout = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Kid(models.Model):
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=35)
    allowance_earned = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Kid_Chore(models.Model):
    kid = models.ForeignKey(Kid, on_delete= models.CASCADE, null=True)
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null=True)
    chore= models.ForeignKey(Chore, on_delete=models.DO_NOTHING, null=True)
    day_of_the_week = models.CharField(max_length=12)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

### run the following command 'python manage.py migrate'
### run the following command 'python3 manage.py makemigrations' then run 'python3 manage.py migrate'


