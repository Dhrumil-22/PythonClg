# Django Project Setup & Commands Guide

## Project Structure Overview

```
studentcorner/                          (Root Project Directory)
├── manage.py                           (Django command-line management script)
├── db.sqlite3                          (SQLite Database - stores all data)
│
├── studentcorner/                      (Project Configuration Folder)
│   ├── urls.py                         (Main URL routing - connects URLs to views)
│   ├── settings.py                     (Project settings & configuration)
│   ├── wsgi.py                         (Web Server Interface)
│   └── asgi.py                         (Async Web Server Interface)
│
├── grades/                             (App 1 - Student Grades Management)
│   ├── models.py                       (Grade model - database table definition)
│   ├── views.py                        (home() and marksheet() functions)
│   ├── admin.py                        (Register Grade in admin panel)
│   ├── templates/
│   │   ├── home.html                   (Homepage template)
│   │   └── marksheet.html              (Grades display template)
│   └── migrations/                     (Database migration files)
│
└── circluars/                          (App 2 - College Circulars/Announcements)
    ├── models.py                       (Currently empty - for future use)
    ├── views.py                        (index() function)
    ├── admin.py                        (Admin registration)
    ├── templates/
    │   └── index.html                  (Circulars display template)
    └── migrations/                     (Database migration files)
```

---

## File Connections & Data Flow

### 1. URL → View → Template → Response

```
User visits URL
    ↓
urls.py (matches URL pattern)
    ↓
views.py (executes view function)
    ↓
models.py (queries database if needed)
    ↓
templates/html (renders with data)
    ↓
HTML response sent to browser
```

### 2. How Files Connect

**Example: User visits http://localhost:8000/grades/?search=john**

1. **urls.py** matches: `path('grades/', views.marksheet, name='marksheet')`
2. **views.py** executes: `marksheet(request)` function
3. Inside marksheet():
   - Gets search parameter: `serachitme = request.GET.get('search')`
   - Queries **models.py**: `Grade.objects.filter(name__icontains='john')`
   - Database returns matching grades
   - Passes to template: `render(request, 'marksheet.html', {'marks': marks})`
4. **marksheet.html** displays the grades
5. Browser shows the results

---

## Essential Commands to Run the Project

### Step 1: Initial Setup (One-time only)

```bash
# Navigate to project directory
cd "c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\DJANGO PB\studentcorner"

# Install Django (if not installed)
pip install django

# Check Django version
python -m django --version
```

### Step 2: Create Database

```bash
# Create migration files from models
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Output: Creates db.sqlite3 with tables for Grade, User, etc.
```

### Step 3: Create Admin User (Superuser)

```bash
# Create admin account to access admin panel
python manage.py createsuperuser

# Prompts:
# - Username: (your username)
# - Email: (your email)
# - Password: (your password)
# - Password (again): (confirm password)

# Example:
# Username: admin
# Email: admin@example.com
# Password: admin123
```

### Step 4: Start Development Server

```bash
# Start the server
python manage.py runserver

# Output will show:
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK (on Windows) or CTRL-C (Mac/Linux)
```

### Step 5: Access the Project

- **Homepage**: http://127.0.0.1:8000/
- **Grades Page**: http://127.0.0.1:8000/grades/
- **Search Grades**: http://127.0.0.1:8000/grades/?search=john
- **Circulars**: http://127.0.0.1:8000/circular/
- **Admin Panel**: http://127.0.0.1:8000/admin/
  - Login with superuser credentials created in Step 3
  - Add grades through admin interface

---

## File-by-File Explanation

### 1. **models.py** (grades app)
- **Purpose**: Defines database table structure
- **Contains**: Grade model with fields (name, rollno, sem, date, spi)
- **When used**: 
  - Creating/updating database tables
  - Querying data in views
- **Commands**:
  ```bash
  python manage.py makemigrations    # Create migration files
  python manage.py migrate           # Apply to database
  ```

### 2. **admin.py** (grades app)
- **Purpose**: Register models with Django admin panel
- **Contains**: `admin.site.register(Grade)`
- **When used**: Accessing http://localhost:8000/admin/
- **Function**: Provides web interface to add/edit/delete grades

### 3. **views.py** (grades app)
- **Purpose**: Handle HTTP requests and return responses
- **Contains**: 
  - `home(request)` - Shows homepage
  - `marksheet(request)` - Shows grades with search filter
- **When used**: Every time a URL is visited
- **Database queries**: Uses `Grade.objects.filter()` and `Grade.objects.all()`

### 4. **urls.py** (studentcorner - main configuration)
- **Purpose**: Map URLs to view functions
- **Contains**: URL patterns for entire project
- **When used**: Django reads this when server starts
- **Routes**:
  - `/` → home view
  - `/grades/` → marksheet view
  - `/circular/` → circulars index view
  - `/admin/` → admin panel

### 5. **settings.py** (studentcorner - main configuration)
- **Purpose**: Project-wide configuration
- **Contains**:
  - INSTALLED_APPS: List of enabled apps ('grades', 'circluars')
  - DATABASES: Database configuration (SQLite3)
  - TEMPLATES: Template directories and settings
  - SECRET_KEY: Security key for sessions
  - DEBUG: Development/production mode
- **When used**: Loaded when Django starts
- **Affects**: Entire project

### 6. **circluars/views.py**
- **Purpose**: Handle circulars/announcements requests
- **Contains**: `index(request)` function
- **When used**: User visits `/circular/` URL
- **Currently**: Shows simple template (can be enhanced with database queries)

### 7. **circluars/models.py**
- **Purpose**: Define circulars data structure
- **Currently**: Empty (template provided with example)
- **Future use**: Can add Circular model to store announcements in database

---

## Common Commands Reference

```bash
# Start server
python manage.py runserver

# Create database migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser

# Access admin panel
# http://localhost:8000/admin/

# Collect static files (CSS, JS, images)
python manage.py collectstatic

# Show all database migrations
python manage.py showmigrations

# Delete all data and reset database
python manage.py flush

# Run tests
python manage.py test

# Create new app
python manage.py startapp appname

# Check for issues
python manage.py check
```

---

## Data Flow Example: Adding a Student Grade

### Step 1: User adds grade in Admin Panel
- Visit: http://localhost:8000/admin/
- Login with superuser
- Click "Grades" → "Add Grade"
- Fill form: name, rollno, sem, date, spi
- Click "Save"

### Step 2: Data is saved
- admin.py processes the form
- Grade model creates database record in db.sqlite3
- grades_grade table gets new row

### Step 3: User views grades
- Visit: http://localhost:8000/grades/
- urls.py matches pattern: `path('grades/', views.marksheet)`
- views.py executes: `marks = Grade.objects.all()`
- Database returns all grades
- marksheet.html displays the grades

---

## Complete Workflow Summary

```
┌─────────────────────────────────────────────────────────────┐
│              DJANGO REQUEST-RESPONSE CYCLE                  │
└─────────────────────────────────────────────────────────────┘

1. USER VISITS URL
   └─→ Browser: http://localhost:8000/grades/

2. URL ROUTING (urls.py)
   └─→ Matches: path('grades/', views.marksheet, name='marksheet')

3. VIEW EXECUTION (views.py)
   └─→ Calls: marksheet(request) function
   └─→ Gets search parameter from URL
   └─→ If search: Grade.objects.filter(name__icontains=search)
   └─→ Else: Grade.objects.all()

4. DATABASE QUERY (models.py)
   └─→ Grade model queries db.sqlite3
   └─→ Returns matching records

5. TEMPLATE RENDERING (marksheet.html)
   └─→ Receives marks data in context
   └─→ Displays grades in HTML format
   └─→ {{ marks }} variable contains data

6. RESPONSE
   └─→ HTML page sent to browser
   └─→ User sees rendered page

┌─────────────────────────────────────────────────────────────┐
│                      ADMIN PANEL FLOW                        │
└─────────────────────────────────────────────────────────────┘

1. USER LOGS INTO ADMIN
   └─→ Browser: http://localhost:8000/admin/

2. ADMIN INTERFACE (admin.py registered Grade)
   └─→ Django auto-generates CRUD forms

3. USER ADDS/EDITS/DELETES GRADE
   └─→ admin.py processes form submission

4. DATABASE UPDATE (models.py & db.sqlite3)
   └─→ Grade record created/updated/deleted

5. CONFIRMATION
   └─→ Admin panel shows success message
```

---

## Troubleshooting Common Issues

### Issue: "No such table: grades_grade"
**Solution**: Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution**: Install Django
```bash
pip install django
```

### Issue: "Admin page shows nothing"
**Solution**: Make sure Grade is registered in admin.py
```python
admin.site.register(Grade)
```

### Issue: "Search doesn't work"
**Solution**: Check views.py - marksheet function uses `name__icontains`
```python
marks = Grade.objects.filter(name__icontains=serachitme)
```

### Issue: "Port 8000 already in use"
**Solution**: Run on different port
```bash
python manage.py runserver 8001
```

---

## Quick Start (TL;DR)

```bash
# 1. Navigate to project
cd "c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\DJANGO PB\studentcorner"

# 2. Setup database
python manage.py makemigrations
python manage.py migrate

# 3. Create admin user
python manage.py createsuperuser

# 4. Start server
python manage.py runserver

# 5. Access:
# - Homepage: http://localhost:8000/
# - Grades: http://localhost:8000/grades/
# - Admin: http://localhost:8000/admin/
```

---

## Next Steps for Enhancement

1. **Add Circular Model** - Uncomment example in circluars/models.py
2. **Add Search** - Already works for grades by student name
3. **Add Filters** - Filter by semester, date, SPI range
4. **Add Styling** - Add CSS to templates for better UI
5. **Add Upload** - Allow file uploads for circulars
6. **Add Authentication** - Restrict admin access to certain users
7. **Add Pagination** - Show grades in pages instead of all at once
