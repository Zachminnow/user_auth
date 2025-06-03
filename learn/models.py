from django.db import models


# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.message


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"


