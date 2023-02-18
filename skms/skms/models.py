from django.db import models

class UserAccount(models.Model):
    

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices= (('Active','Active'), ('Inactive','Inactive')), default='Active')
    type = models.CharField(max_length=255, choices= (('User','User'), ('Expert','Expert')), default='User')

    def __str__(self):
        return self.username
