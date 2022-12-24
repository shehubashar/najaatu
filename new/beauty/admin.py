from django.contrib import admin
from .models import Service, Person,Time_BOOK

# Register your models here.
admin.site.register([Service,Person,Time_BOOK])