from django.db import models


# Create your models here.
class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name
