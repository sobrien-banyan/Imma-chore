from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)




class Chore(models.Model):
    name = models.CharField(max_length=35)
    descriotion = models.CharField(max_length=35)
    payout = models.IntegerField(blank=True, null=True)
    day_of_the_week = models.DateTimeField()
    is_complete = models.BooleanField(default=False)

class Kid(models.Model):
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE)
    name = models.CharField(max_length=35)
    allowance_earned = models.IntegerField(blank=True, null=True)
    chore = models.ManyToManyField(Chore)