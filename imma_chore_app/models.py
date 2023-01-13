from django.db import models

# Create your models here.

class Parent(models.Model):
    '''two fields, name can store up to 30 characters'''
    name = models.CharField(max_length=30)
    '''name is used to store the name of the Parent'''
    created_at = models.DateTimeField(auto_now_add=True)
    '''will automatically set date and time when recorded'''

class Chore(models.Model):
    '''four fields - name can store up to 35 characters '''
    name = models.CharField(max_length=35)
    '''is used to store the name of the chore'''
    description = models.CharField(max_length=35)
    '''used to store the description of the chore'''
    payout = models.IntegerField(blank=True, null=True)
    '''can store integers and stores the payments for the chore'''
    created_at = models.DateTimeField(auto_now_add=True)
    '''will automatically set date and time when recorded'''

class Kid(models.Model):
    '''four fields - the parent is the foreign key which creates 
    a Many to Many relationship between Kid and Parent Models'''
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null=True)
    '''Cascade in this sense means if the parent is deleted, so is the kid associated'''
    name = models.CharField(max_length=35)
    '''can holds up to 35 characters and stores the name'''
    allowance_earned = models.IntegerField(blank=True, null=True)
    '''can store integers and is used to record payment for chore'''
    created_at = models.DateTimeField(auto_now_add=True)
    '''will automatically set date and time when recorded'''

class Kid_Chore(models.Model):
    '''five fields'''
    kid = models.ForeignKey(Kid, on_delete= models.CASCADE, null=True)
    '''kid field is the foreign key, creates a many to one relationship between
    Kid_Chore and Chore '''
    chore= models.ForeignKey(Chore, on_delete=models.DO_NOTHING, null=True)
    '''if chore is deleted it will not effect kid_chore'''
    day_of_the_week = models.CharField(max_length=12)
    '''can hold 12 characters that store day of the week'''
    is_complete = models.BooleanField(default=False)
    '''a boolean describing whether or not a chore is completed or not'''
    created_at = models.DateTimeField(auto_now_add=True)
    '''will automatically set date and time when recorded'''