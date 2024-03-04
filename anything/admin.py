from django.contrib import admin
from anything.models import Users,Member,Booking
from anything.models import Products

# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Member)
admin.site.register(Booking)
