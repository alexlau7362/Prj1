# Update database model to backend
from django.contrib import admin

# Register your models here.

#. same level import class
from .models import Listing
# register the class to backend
admin.site.register(Listing)