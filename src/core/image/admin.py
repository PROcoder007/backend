from django.contrib import admin

# Register your models here.
from .models import Item ,Document

admin.site.register(Item)
admin.site.register(Document)
