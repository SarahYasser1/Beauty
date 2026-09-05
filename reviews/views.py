# reviews/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Review


@login_required
def add_review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        Review.objects.create(
            student=request.user.student_profile,
            course=course,
            rating=request.POST.get('rating'),
            comment=request.POST.get('comment'),
        )
        return redirect('course_detail', pk=course.id)
    return render(request, 'reviews/add_review.html', {'course': course})

# Create your views here.
