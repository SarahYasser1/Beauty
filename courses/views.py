from django.shortcuts import render, get_object_or_404
from .models import Course, Category, Lesson


def course_list(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses, 'categories': categories})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})
