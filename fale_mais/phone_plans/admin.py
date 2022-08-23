from django.contrib import admin
from .models import codeDDD, Charge, PhonePlan

@admin.register(codeDDD)
class codeDDDAdmin(admin.ModelAdmin):
    list_display = ['code', 'city', 'state']
    search_fields = ['city', 'state']

@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ['origin', 'destiny', 'tax']
    search_fields = ['origin', 'destiny']

@admin.register(PhonePlan)
class PhonePlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'time_limit']
    search_fields = ['name']
