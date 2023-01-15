from django.db import models

# Create your models here.
# A parent model will need a name only for functionality
class Parent(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
#Chores will be broken down into name, description, and payout for functionality, needs parent id for accessibility
class Chore(models.Model):
    name = models.CharField(max_length=35)
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null=True)
    description = models.CharField(max_length=35)
    payout = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
#Kid formn eeds name and allowance for functionality, also for acsessibility needs parent id
class Kid(models.Model):
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=35)
    allowance_earned = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
#form needs kid, parent, and chore for accessibility and chore day oif the week and is complete for functionality
class Kid_Chore(models.Model):
    kid = models.ForeignKey(Kid, on_delete= models.CASCADE, null=True)
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null=True)
    chore= models.ForeignKey(Chore, on_delete=models.DO_NOTHING, null=True)
    day_of_the_week = models.CharField(max_length=12)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)