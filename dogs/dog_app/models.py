from django.contrib.auth.models import AbstractUser

from django.db import models


class MyUser(AbstractUser):

    designation_choices = (
        ('emp','Employee'),
        ('manager','Manager'),
        ('client','Client'),
        ('admin','Admin'),
    )

    department_choices = (
        ('hr','HR'),
        ('marketing','Marketing'),
        ('accounts','Accounts'),
    )

    gender_choice = (
        ('M','Male'),
        ('F','Female'),
        ('other','Other'),
    )
    username            = models.CharField(unique=True, blank=True, max_length=50)
    email               = models.EmailField(unique=False, blank=False)
    first_name          = models.CharField(blank=False, max_length=35)
    middle_name         = models.CharField(blank=True, max_length=35)
    last_name           = models.CharField(blank=True, max_length=35)
    age                 = models.IntegerField(null=True, blank=True)
    contact             = models.IntegerField(null=True, blank=True)
    salary              = models.IntegerField(null=True, blank=True)
    created_on          = models.DateTimeField(auto_now_add=True)
    date_of_joining     = models.DateField(blank=True, null=True)
    department          = models.CharField(default=None, choices=department_choices, max_length=35)
    designation         = models.CharField(default=None, choices=designation_choices, max_length=35)
    gender              = models.CharField(default='M', choices=gender_choice, max_length=10, null=True, blank=True)




class Dog(models.Model):
    name = models.CharField(max_length=45)
    breed = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering= ['name']


