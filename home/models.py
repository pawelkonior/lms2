from django.db import models


class ContactMessage(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f'{self.fullname}, {self.message[:10]}'
