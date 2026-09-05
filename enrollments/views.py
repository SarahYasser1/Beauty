
# Create your views here.
# enrollments/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Enrollment


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    Enrollment.objects.get_or_create(student=request.user.student_profile, course=course)
    return redirect('course_detail', pk=course.id)


@login_required
def my_enrollments(request):
    enrollments = Enrollment.objects.filter(student=request.user.student_profile)
    return render(request, 'enrollments/my_enrollments.html', {'enrollments': enrollments})