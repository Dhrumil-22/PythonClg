from django.contrib import admin
from .models import Grade

# ==================== ADMIN REGISTRATION ====================
# This file registers Django models with the admin panel
# Admin Panel URL: http://localhost:8000/admin/
#
# What is Admin Panel?
# - Built-in Django feature for managing database records
# - Create, Read, Update, Delete (CRUD) operations
# - Accessible after login with superuser account
#
# HOW IT WORKS:
# 1. Model (Grade) is defined in models.py
# 2. Model is registered here with admin.site.register()
# 3. Admin panel automatically creates interface for Grade management
# 4. Can add/edit/delete student grades through web interface
#
# CONNECTION:
# Admin.py (registers) → Models.py (defines) → Database (stores)

# Register the Grade model with Django admin
# This line makes Grade visible in the admin dashboard
admin.site.register(Grade)

# ==================== OPTIONAL: CUSTOM ADMIN CONFIGURATION ====================
# You can customize the admin interface (optional):
#
# class GradeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'rollno', 'sem', 'spi']  # Columns to show in list
#     list_filter = ['sem', 'date']                     # Filter options
#     search_fields = ['name', 'rollno']                # Searchable fields
#     ordering = ['-date']                              # Default sorting
#
# admin.site.register(Grade, GradeAdmin)
#
# After uncommenting above:
# - Admin panel will show name, rollno, sem, spi columns
# - Can filter by semester and date
# - Can search by name and roll number

# ==================== ACCESS ADMIN ====================
# 1. Create superuser: python manage.py createsuperuser
# 2. Start server: python manage.py runserver
# 3. Go to: http://localhost:8000/admin/
# 4. Login with superuser credentials
# 5. Click "Grades" → Add/Edit/Delete records
