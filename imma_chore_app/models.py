from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class Chore(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=35)
    payout = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Kid(models.Model):
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=35)
    allowance_earned = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Kid_Chore(models.Model):
    kid = models.ForeignKey(Kid, on_delete= models.CASCADE, null=True)
    chore= models.ForeignKey(Chore, on_delete=models.DO_NOTHING, null=True)
    day_of_the_week = models.CharField(max_length=12)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)