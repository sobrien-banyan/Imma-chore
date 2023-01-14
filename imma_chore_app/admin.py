from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Parent)
admin.site.register(Kid)
admin.site.register(Chore)
admin.site.register(Kid_Chore)