from django.shortcuts import render

# ==================== CIRCULARS/ANNOUNCEMENTS VIEW ====================
# This file handles views for the circulars app
# Circulars = College announcements/notifications/circular letters
#
# CONNECTION FLOW:
# URL: /circular/ → urls.py → circluars/views.py (this file) → index.html

# ==================== INDEX VIEW ====================
def index(request):
    """
    CIRCULARS/ANNOUNCEMENTS PAGE VIEW
    
    URL: http://localhost:8000/circular/
    Function Name in urls.py: cv.index (imported as cv)
    URL Name: 'index'
    Template Used: index.html
    
    What it does:
    - Displays college circulars/announcements
    - Simple page view (no database queries currently)
    - Renders index.html template
    
    How to use in HTML:
    <a href="{% url 'index' %}">Circulars</a>
    """
    return render(request, 'index.html')


# ==================== FUTURE ENHANCEMENTS ====================
# You can add database queries here:
#
# from .models import Circular
#
# def index(request):
#     circulars = Circular.objects.all().order_by('-date')
#     return render(request, 'index.html', {'circulars': circulars})
#
# This would fetch all circulars from database and display them