from django.db import models

# ==================== CIRCULARS MODELS ====================
# This file defines database models for circulars/announcements
# Currently empty - no models defined yet
#
# EXAMPLE: You could add a Circular model like this:
#
# class Circular(models.Model):
#     title = models.CharField(max_length=200)      # Circular title
#     content = models.TextField()                   # Full circular text
#     date = models.DateField()                      # Published date
#     category = models.CharField(max_length=100)   # Academic, Event, etc.
#     attachment = models.FileField(upload_to='circulars/')  # PDF attachment
#     
#     def __str__(self):
#         return self.title
#
# After creating model:
# 1. Run: python manage.py makemigrations
# 2. Run: python manage.py migrate
# 3. Register in admin.py: admin.site.register(Circular)
# 4. Use in views.py to fetch and display circulars
