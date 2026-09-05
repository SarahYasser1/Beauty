# enrollments/admin.py
from django.contrib import admin
from .models import Enrollment, Payment, Progress

admin.site.register(Enrollment)
admin.site.register(Payment)
admin.site.register(Progress)