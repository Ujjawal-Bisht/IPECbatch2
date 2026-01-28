from django.db import models
from django import forms

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    data_of_entry = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        return f"{self.title} by {self.author}"

# # user
# class User(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     mobile_number = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(unique=True)
#     book_issued = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
#     address = models.TextField()
#     book_issued_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.username