from django.db import models

# Create your models here.









class Kid(model.Model):
    parent = model.ForeignKey()
    name = models.CharField(max_length=35)
    allowance_earned = models.IntegerField()


class Chore(model.Model):
