from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

### student model start here ###
CLASS_STANDARD = (
    ('DS', 'Select the class'),
    ('1st' , 'FIRST'),
    ('2nd', 'SECOND'),
    ('3rd', 'THIRD'),
    ('4th', 'FOUR'),
    ('5th', 'FIFTH'),
    ('6th', 'SIXTH'),
    ('7th', 'SEVENTH'),
    ('8th', 'EIGTHTH'),
    ('9th', 'NINETH'),
    ('10th', 'TENTH'),
    ('11th', 'ELEVENTH'),
    ('12th', 'TWELVETH')
)

CLASS_SECTION = (
    ('DS', 'Select the section'),
    ('A', 'SECTION A'),
    ('B', 'SECTION B'),
    ('C', 'SECTION C'),
    ('D', 'SECTION D'),
    ('E', 'SECTION E')
)

STREAM = (
    ('Not specified', 'Select the Stream if your class greater than 10'),
    ('SCIENCE', 'SCIENCE'),
    ('COMMERCE', 'COMMERCE'),
    ('ARTS', 'ARTS')
)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    standard = models.CharField(max_length=5, choices=CLASS_STANDARD)
    class_section = models.CharField(max_length=5, choices=CLASS_SECTION)
    stream = models.CharField(max_length=14, choices=STREAM)
    roll_no = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.user)

### student model end here ###



### teacher model start here ###

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length=100)
    classes_taught = models.CharField(max_length=100)
    number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user)

### teacher model end here ###