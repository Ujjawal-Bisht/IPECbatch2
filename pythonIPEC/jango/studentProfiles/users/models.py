from django.db import models

# Create your models here.

class Students(models.Model):
    branchChoice = [
    ('CSE', "COMPUTER SCIENCE ENGINEERING"),
    ('IT', "INFORMATION TECHNOLOGY"),
    ('EE', "ELECTRICAL ENGINEERING")
    ]

    rollno = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    branch = models.CharField(choices = branchChoice)
    email = models.EmailField()
    dob = models.DateField()

    def __str__(self):
        return self.name
    
    