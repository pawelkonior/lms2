from django.contrib.auth import get_user_model
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='courses_creator')

    def __str__(self):
        return self.title
