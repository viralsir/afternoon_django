from django.contrib import admin
from .models import flight
from .models import airport
# Register your models here.
admin.site.register(airport)
admin.site.register(flight)