# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StudentProfile


@login_required
def profile_view(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})