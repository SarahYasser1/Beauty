# enrollments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('my-enrollments/', views.my_enrollments, name='my_enrollments'),
]