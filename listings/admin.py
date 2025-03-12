# Update database model to backend
from django.contrib import admin
from django.forms import NumberInput
from django.db import models

# Register your models here.

#. same level import class
from .models import Listing
# add 2025-3-5 for showing more realtor details in admin page
class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','list_date','realtor')
    list_display_links = 'id', 'title'
    list_filter = 'realtor',      # < - add filter
    list_editable = 'is_published',
    search_fields = 'title', 'description', 'address', 'price'
    list_per_page = 25
    ordering = ['-id']
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size' : '10'})},
    }

# register the class to backend
admin.site.register(Listing, ListingAdmin)