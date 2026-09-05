# reviews/models.py
from django.db import models
from accounts.models import StudentProfile
from courses.models import Course


class Review(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.rating}"
