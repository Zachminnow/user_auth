from django.db import models
from django.contrib.auth.models import User


# One-to-one: Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s profile"


# One-to-many: Instructor -> Courses
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='courses')

    def __str__(self):
        return self.instructor


# Many-to-Many: Student <-> Courses
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.username
