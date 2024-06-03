from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
)
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices = STATUS,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
