from django.db import models
from django_extensions.db.models import TimeStampedModel


class Task(TimeStampedModel):
    # Priority Choices
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=LOW)
    due_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
