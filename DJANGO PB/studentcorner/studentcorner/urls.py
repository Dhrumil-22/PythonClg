"""
URL configuration for studentcorner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# ==================== IMPORTS ====================
# Import admin: This provides Django's built-in admin interface (admin dashboard)
from django.contrib import admin

# Import path: This is used to define URL routes using the path() function
from django.urls import path

# Import views from grades app: These are functions that handle HTTP requests for grades-related pages
from grades import views

# Import views from circluars app with alias 'cv': These handle HTTP requests for circular-related pages
# (Note: 'circluars' appears to be a typo for 'circulars')
from circluars import views as cv


# ==================== PROJECT STRUCTURE OVERVIEW ====================
# This is the MAIN/ROOT URL configuration file for the entire 'studentcorner' Django project
# Located in: studentcorner/studentcorner/urls.py
#
# PROJECT APPS:
# 1. grades - Displays student grades/marks (has models, views, templates)
# 2. circluars - Displays college circulars/announcements (has views, templates)
#
# How it works:
# 1. User enters a URL in browser (e.g., http://localhost:8000/grades/)
# 2. Django matches it against urlpatterns (below)
# 3. If match found, the corresponding view function is executed
# 4. View function processes data and renders an HTML template
# 5. HTML page is sent back to the user's browser


# ==================== URL PATTERNS ====================
# This list defines all the routes (URLs) for the entire project
urlpatterns = [
    # ---- DJANGO ADMIN ROUTE ----
    # URL: http://localhost:8000/admin/
    # Purpose: Access Django's built-in admin dashboard to manage database records
    # Features: Create, read, update, delete (CRUD) operations for all registered models
    path('admin/', admin.site.urls),
    
    
    # ---- HOME PAGE ROUTE ----
    # URL: http://localhost:8000/
    # Function Called: views.home() [from grades/views.py]
    # What it does:
    #   - Displays the home/landing page
    #   - Renders 'home.html' template
    #   - No database queries
    # URL Name: 'home' (used in templates: {% url 'home' %})
    path('', views.home, name='home'),
    
    
    # ---- GRADES/MARKSHEET ROUTE ----
    # URL: http://localhost:8000/grades/
    # Function Called: views.marksheet() [from grades/views.py]
    # What it does:
    #   - Displays student marks/grades
    #   - Gets search parameter from URL query string (e.g., ?search=studentname)
    #   - If search provided: filters Grade objects by name (case-insensitive)
    #   - If no search: shows all grades from database
    #   - Renders 'marksheet.html' template with filtered/all marks
    # URL Name: 'marksheet' (used in templates: {% url 'marksheet' %})
    path('grades/', views.marksheet, name='marksheet'),
    
    
    # ---- CIRCULARS ROUTE ----
    # URL: http://localhost:8000/circular/
    # Function Called: cv.index() [from circluars/views.py, imported as 'cv']
    # What it does:
    #   - Displays college circulars/announcements/notifications
    #   - Renders 'index.html' template
    #   - No database queries in current implementation
    # URL Name: 'index' (used in templates: {% url 'index' %})
    path('circular/', cv.index, name='index')
]


# ==================== HOW CONNECTIONS WORK ====================
#
# REQUEST FLOW EXAMPLE:
# 1. User visits: http://localhost:8000/grades/?search=john
# 2. Django URL router checks urlpatterns from top to bottom
# 3. Matches: path('grades/', views.marksheet, name='marksheet')
# 4. Executes: views.marksheet(request) from grades/views.py
# 5. Inside marksheet():
#    - Gets 'search' parameter from request.GET
#    - If search exists: queries Grade model with filter
#    - If no search: gets all grades from Grade model
#    - Passes marks to template context
# 6. Renders: marksheet.html with the grades data
# 7. Returns HTML to user's browser
#
# DATA FLOW:
# URL Route → View Function → Database Query (if needed) → Template → HTML Response
#
# PROJECT STRUCTURE:
# studentcorner/                    (Main project folder)
#  ├── manage.py                    (Command-line management script)
#  ├── db.sqlite3                   (Database file - stores all data)
#  ├── studentcorner/               (Project settings folder - THIS FOLDER)
#  │   ├── urls.py                  (This file - main URL configuration)
#  │   ├── settings.py              (Project configuration, installed apps, database)
#  │   ├── wsgi.py                  (Web server interface)
#  │   └── asgi.py                  (Async web server interface)
#  ├── grades/                      (App 1 - Student Grades)
#  │   ├── views.py                 (home(), marksheet() functions)
#  │   ├── models.py                (Grade model - database table structure)
#  │   ├── templates/marksheet.html (HTML template for marks display)
#  │   └── templates/home.html      (HTML template for home page)
#  └── circluars/                   (App 2 - College Circulars)
#      ├── views.py                 (index() function)
#      ├── models.py                (Circular models if used)
#      └── templates/index.html     (HTML template for circulars)
#
# IMPORTANT: This urls.py is in the project configuration folder (studentcorner/studentcorner/)
# It is the MAIN/MASTER URL file for the entire project
