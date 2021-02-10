from django.contrib import admin

from .models import Invoice, Item

admin.site.register(Invoice)
admin.site.register(Item)