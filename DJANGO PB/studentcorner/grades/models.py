from django.db import models

# ==================== GRADE MODEL ====================
# This file defines the database structure/schema for student grades
# A Model in Django represents a database table
# Each attribute becomes a column in the database table
# This model automatically creates a 'grades_grade' table in SQLite database
#
# CONNECTION FLOW:
# 1. Model defined here → 2. Registered in admin.py → 3. Accessed in views.py → 4. Displayed in templates
#
# HOW IT WORKS:
# - When Django starts, it reads this model and creates/updates the database table
# - Each Grade instance = one row in the database
# - Data is stored in: db.sqlite3 (the database file)

class Grade(models.Model):
    """
    Grade Model - Stores student marks and performance data
    Database Table Name: grades_grade (automatically created by Django)
    """
    
    # Student Name - text field, max 200 characters
    # Example: "John Doe"
    name = models.CharField(max_length=200)
    
    # Student Roll Number - integer field (no decimals)
    # Example: 101, 102, 103
    rollno = models.IntegerField()
    
    # Semester Number - which semester (1, 2, 3, 4, etc.)
    # Example: 4 (for 4th semester)
    sem = models.IntegerField()
    
    # Date of grade - stores the date when grades were issued
    # Example: 2025-06-01
    date = models.DateField()
    
    # SPI (Semester Performance Index) - student's GPA/performance score
    # blank=True means this field is optional (can be empty)
    # Example: 7.5, 8.2, 9.1
    spi = models.FloatField(blank=True)
    
    class Meta:
        # (Optional) You can add metadata here
        # Example: ordering = ['-date']  to sort by date descending
        pass
    
    def __str__(self):
        """String representation - what you see in admin panel"""
        return f"{self.name} - Sem {self.sem} - SPI: {self.spi}"

# ==================== DATABASE COMMANDS ====================
# To create this model in database:
# 1. python manage.py makemigrations  (creates migration file)
# 2. python manage.py migrate          (applies changes to database)
#
# To use this model in code:
# from grades.models import Grade
# Grade.objects.all()              - Get all grades
# Grade.objects.filter(name='John') - Search by name
# Grade.objects.create(name='John', rollno=101, sem=4, date='2025-06-01', spi=8.5)
