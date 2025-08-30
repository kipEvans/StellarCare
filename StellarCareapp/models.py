from django.db import models

# Create your models here.
class Appoint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    date = models.DateField()
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField()
    message = models.TextField()

    def __str__(self):
        return self.name