from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10)
    description = models.TextField()
    # One-to-many relationship(FOREIGNKEY) author = many posts
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
class Course(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToMany(Course)

# One-to-one relationship(OneToOneField)
A user has one profile and a profile belongs to one user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
"""
