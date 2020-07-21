from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length = 60, unique=True)
    school = models.CharField(max_length = 30)
    password = models.CharField(max_length = 6)
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length = 30)


    def __str__(self):
        return self.firstName + " " + self.lastName
