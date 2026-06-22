from django.shortcuts import render
from .models import Grade

# ==================== VIEWS.PY EXPLANATION ====================
# This file contains VIEW FUNCTIONS that handle HTTP requests
# A View = Function that receives a request and returns a response (HTML page)
#
# CONNECTION FLOW:
# URL (urls.py) → View Function (this file) → Database Query (models.py) → Template (HTML) → Response
#
# HOW VIEWS WORK:
# 1. User visits a URL (e.g., http://localhost:8000/)
# 2. Django URL router (urls.py) finds matching path
# 3. Executes corresponding view function here
# 4. View processes data and renders template
# 5. HTML is sent back to user's browser

# ==================== HOME VIEW ====================
def home(request):
    """
    HOME PAGE VIEW
    
    URL: http://localhost:8000/
    Function Name in urls.py: views.home
    URL Name: 'home'
    Template Used: home.html
    
    What it does:
    - Handles request when user visits homepage
    - No database queries (simple page)
    - Renders home.html template
    
    How to use in HTML:
    <a href="{% url 'home' %}">Home</a>
    """
    return render(request, 'home.html')


# ==================== MARKSHEET VIEW ====================
def marksheet(request):
    """
    STUDENT GRADES/MARKSHEET VIEW
    
    URL: http://localhost:8000/grades/
    URL with search: http://localhost:8000/grades/?search=john
    Function Name in urls.py: views.marksheet
    URL Name: 'marksheet'
    Template Used: marksheet.html
    Database Model Used: Grade (from models.py)
    
    What it does:
    - Displays all student grades/marks
    - Supports searching by student name
    - Queries Grade model from database
    - Passes data to template for display
    
    STEP-BY-STEP EXECUTION:
    """
    
    # STEP 1: Get search parameter from URL query string
    # URL format: http://localhost:8000/grades/?search=studentname
    # request.GET is a dictionary of URL parameters
    # If no search provided, serachitme = None
    serachitme = request.GET.get('search')
    # (Note: 'serachitme' is a typo for 'search_item', but keeping as-is in your code)
    
    # STEP 2: Check if user provided search term
    if serachitme:
        # SEARCH MODE: Filter grades by student name
        # Grade.objects.filter() → Query the Grade model/table
        # name__icontains → Search for name containing search term (case-insensitive)
        #   'i' means case-insensitive
        #   'contains' means substring match
        # Example: searching 'john' finds 'John', 'JOHN', 'john', 'Johnson'
        marks = Grade.objects.filter(name__icontains=serachitme)
    else:
        # NO SEARCH: Show all grades from database
        # Grade.objects.all() → Returns all Grade records from database
        marks = Grade.objects.all()
    
    # STEP 3: Render template with context data
    # Context = {'marks': marks} is passed to template
    # In marksheet.html, you can access marks with {{ marks }} variable
    return render(request, 'marksheet.html', {'marks': marks})


# ==================== DATABASE QUERY METHODS ====================
# Other Grade queries you can use:
#
# Grade.objects.all()                    → Get ALL grades
# Grade.objects.filter(sem=4)            → Get grades for semester 4
# Grade.objects.filter(name='John')      → Exact name match
# Grade.objects.filter(name__icontains='john')  → Case-insensitive search
# Grade.objects.filter(spi__gte=8.0)     → SPI greater than or equal to 8.0
# Grade.objects.get(rollno=101)          → Get single student by roll number
# Grade.objects.filter(sem=4).count()    → Count how many grades in sem 4
# Grade.objects.filter(sem=4).order_by('-spi')  → Sort by SPI descending


# ==================== TEMPLATE CONTEXT ====================
# What gets passed to templates:
# {{ marks }}          → List of all Grade objects
# {{ marks.count }}    → Total number of grades
# Loop in template:
#   {% for grade in marks %}
#     {{ grade.name }} - {{ grade.rollno }} - {{ grade.spi }}
#   {% endfor %}
    