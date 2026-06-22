# Complete Django Project Setup - All Commands in Order

## Step-by-Step Commands to Create This Entire Project

### Step 1: Initial Setup & Project Creation

```bash
# Create a folder for your project
mkdir "DJANGO PB"
cd "DJANGO PB"

# Install Django (first time only)
pip install django

# Create Django project
django-admin startproject studentcorner
cd studentcorner

# Verify project was created
python manage.py --version
```

**Result:** Creates `studentcorner/` folder with:
- `manage.py` (command-line tool)
- `studentcorner/` (project settings folder)

---

### Step 2: Create Apps

```bash
# Create grades app
python manage.py startapp grades

# Create circulars app
python manage.py startapp circluars
```

**Result:** Creates two app folders:
- `grades/` with models.py, views.py, admin.py, etc.
- `circluars/` with models.py, views.py, admin.py, etc.

---

### Step 3: Register Apps in settings.py

```bash
# Edit: studentcorner/settings.py
# Add 'grades' and 'circluars' to INSTALLED_APPS list
```

**File: `studentcorner/settings.py`**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grades',          # ← ADD THIS
    'circluars',       # ← ADD THIS
]
```

---

### Step 4: Create Models (Database Structure)

**File: `grades/models.py`**
```python
from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.IntegerField()
    sem = models.IntegerField()
    date = models.DateField()
    spi = models.FloatField(blank=True)
    
    def __str__(self):
        return f"{self.name} - Sem {self.sem} - SPI: {self.spi}"
```

**File: `circluars/models.py`**
```python
from django.db import models

# Create your models here.
# (Leave empty for now, can add Circular model later)
```

---

### Step 5: Create Migrations (Database Schema)

```bash
# Create migration files from models
python manage.py makemigrations

# Output: Creates migration files in grades/migrations/ and circluars/migrations/
```

**Result:** Creates file:
- `grades/migrations/0001_initial.py` (Grade model migration)

---

### Step 6: Apply Migrations to Database

```bash
# Apply migrations to create database tables
python manage.py migrate

# Output: 
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   ... (more migrations)
#   Applying grades.0001_initial... OK
```

**Result:** Creates `db.sqlite3` database file with all tables

---

### Step 7: Register Models in Admin Panel

**File: `grades/admin.py`**
```python
from django.contrib import admin
from .models import Grade

admin.site.register(Grade)
```

**File: `circluars/admin.py`**
```python
from django.contrib import admin

# Register your models here.
```

---

### Step 8: Create Views (Request Handlers)

**File: `grades/views.py`**
```python
from django.shortcuts import render
from .models import Grade

def home(request):
    return render(request, 'home.html')

def marksheet(request):
    serachitme = request.GET.get('search')
    if serachitme:
        marks = Grade.objects.filter(name__icontains=serachitme)
    else:
        marks = Grade.objects.all()
    return render(request, 'marksheet.html', {'marks': marks})
```

**File: `circluars/views.py`**
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

---

### Step 9: Create URL Patterns (URL Routing)

**File: `studentcorner/urls.py`**
```python
from django.contrib import admin
from django.urls import path
from grades import views
from circluars import views as cv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('grades/', views.marksheet, name='marksheet'),
    path('circular/', cv.index, name='index')
]
```

---

### Step 10: Create Templates (HTML Files)

```bash
# Create template directories
mkdir grades/templates
mkdir circluars/templates
```

**File: `grades/templates/home.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home - Student Corner</title>
</head>
<body>
    <h1>Welcome to Student Corner</h1>
    <ul>
        <li><a href="{% url 'marksheet' %}">View Grades</a></li>
        <li><a href="{% url 'index' %}">Circulars</a></li>
    </ul>
</body>
</html>
```

**File: `grades/templates/marksheet.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Grades</title>
</head>
<body>
    <h1>Student Grades - Marksheet</h1>
    
    <form method="get">
        <input type="text" name="search" placeholder="Search student name">
        <button type="submit">Search</button>
    </form>
    
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Roll No</th>
                <th>Semester</th>
                <th>Date</th>
                <th>SPI</th>
            </tr>
        </thead>
        <tbody>
            {% for mark in marks %}
            <tr>
                <td>{{ mark.name }}</td>
                <td>{{ mark.rollno }}</td>
                <td>{{ mark.sem }}</td>
                <td>{{ mark.date }}</td>
                <td>{{ mark.spi }}</td>
            </tr>
            {% empty %}
            <tr><td colspan="5">No grades found</td></tr>
            {% endfor %}
        </tbody>
    </table>
    
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>
```

**File: `grades/templates/index.html`** (or `circluars/templates/index.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Circulars</title>
</head>
<body>
    <h1>College Circulars</h1>
    
    <p>No circulars yet. Check back soon!</p>
    
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>
```

---

### Step 11: Create Superuser (Admin Account)

```bash
# Create admin account
python manage.py createsuperuser

# Prompts:
# Username: admin
# Email: admin@example.com
# Password: admin123
# Password (again): admin123

# Confirmation:
# Superuser created successfully.
```

---

### Step 12: Start Development Server

```bash
# Start the Django development server
python manage.py runserver

# Output:
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK (on Windows)
```

---

## Quick Reference: All Commands in Order

```bash
# 1. Create project folder
mkdir "DJANGO PB"
cd "DJANGO PB"

# 2. Install Django
pip install django

# 3. Create project
django-admin startproject studentcorner
cd studentcorner

# 4. Create apps
python manage.py startapp grades
python manage.py startapp circluars

# 5. Edit settings.py (add apps to INSTALLED_APPS)

# 6. Create models in grades/models.py

# 7. Make migrations
python manage.py makemigrations

# 8. Apply migrations
python manage.py migrate

# 9. Register in admin (edit grades/admin.py and circluars/admin.py)

# 10. Create views (edit grades/views.py and circluars/views.py)

# 11. Create URL patterns (edit studentcorner/urls.py)

# 12. Create template folders
mkdir grades/templates
mkdir circluars/templates

# 13. Create template files (home.html, marksheet.html, index.html)

# 14. Create superuser
python manage.py createsuperuser

# 15. Run server
python manage.py runserver
```

---

## After Server Starts - What You Can Do

```bash
# While server is running (http://127.0.0.1:8000/):

# 1. Add grades via admin panel:
#    http://127.0.0.1:8000/admin/
#    Login with superuser credentials

# 2. View homepage:
#    http://127.0.0.1:8000/

# 3. View all grades:
#    http://127.0.0.1:8000/grades/

# 4. Search grades:
#    http://127.0.0.1:8000/grades/?search=john

# 5. View circulars:
#    http://127.0.0.1:8000/circular/
```

---

## File Structure After All Commands

```
studentcorner/
├── manage.py                    # Django command tool
├── db.sqlite3                   # Database (created by migrate)
│
├── studentcorner/               # Project settings
│   ├── __init__.py
│   ├── settings.py              # (EDITED: added 'grades', 'circluars')
│   ├── urls.py                  # (EDITED: added URL patterns)
│   ├── asgi.py
│   └── wsgi.py
│
├── grades/                      # App 1
│   ├── __init__.py
│   ├── models.py                # (EDITED: created Grade model)
│   ├── views.py                 # (EDITED: created home(), marksheet())
│   ├── admin.py                 # (EDITED: registered Grade)
│   ├── apps.py
│   ├── tests.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py      # (AUTO-CREATED by makemigrations)
│   └── templates/               # (CREATED: folder)
│       ├── home.html            # (CREATED)
│       ├── marksheet.html       # (CREATED)
│       └── index.html           # (CREATED)
│
└── circluars/                   # App 2
    ├── __init__.py
    ├── models.py                # (Empty for now)
    ├── views.py                 # (EDITED: created index())
    ├── admin.py
    ├── apps.py
    ├── tests.py
    ├── migrations/
    │   └── __init__.py
    └── templates/               # (CREATED: folder)
        └── index.html           # (CREATED)
```

---

## Subsequent Development Commands

```bash
# If you modify models and need to update database:
python manage.py makemigrations
python manage.py migrate

# To check for issues:
python manage.py check

# To see all migrations:
python manage.py showmigrations

# To collect static files (CSS, JS, images):
python manage.py collectstatic

# To reset everything (delete all data):
python manage.py flush

# To create another superuser:
python manage.py createsuperuser

# To run tests:
python manage.py test

# To create a new app:
python manage.py startapp appname

# To run shell (Python REPL with Django context):
python manage.py shell
```

---

## Common Command Issues & Solutions

```bash
# Error: "No such table"
# Solution:
python manage.py migrate

# Error: "ModuleNotFoundError: No module named 'django'"
# Solution:
pip install django

# Error: "Port 8000 already in use"
# Solution:
python manage.py runserver 8001

# Error: "Can't find template"
# Solution: Make sure templates folder exists in app directory:
mkdir grades/templates

# Error: "App 'grades' doesn't have a 'models' module"
# Solution: Make sure apps are added to INSTALLED_APPS in settings.py
```

---

## Summary

This document shows **every single command** needed to create your exact Django project from scratch:

1. ✅ Project creation
2. ✅ App creation
3. ✅ Model definition
4. ✅ Database setup (migrations)
5. ✅ Admin registration
6. ✅ Views creation
7. ✅ URL routing
8. ✅ Templates creation
9. ✅ Superuser creation
10. ✅ Server startup

**To recreate this entire project, just follow the commands in order!**
