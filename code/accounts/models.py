# from asyncio.windows_events import NULL
# from curses.ascii import NUL
# from tkinter import CASCADE
from django.db import models
from django.utils import timezone
# Create your models here.
class Clients(models.Model):
    name=models.CharField(max_length=200,null=False)
    phone=models.CharField(max_length=30,null=False)
    profile_link=models.CharField(max_length=200,null=False)
    date_added=models.DateTimeField(default=timezone.now)
class Commande(models.Model):
    about=models.CharField(max_length=500,null=False)
    cout=models.FloatField(null=False)
    prix=models.FloatField(null=False)
    date_ajoutee=models.DateTimeField(default=timezone.now)
    client=models.ForeignKey(Clients,on_delete=models.CASCADE)
    
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    # NbDesCommandes=models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name