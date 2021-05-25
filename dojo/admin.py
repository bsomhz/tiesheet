from django.contrib import admin
from .models import Dojo, Operator, Player


# Register your models here.
@admin.register(Dojo)
class DojoAdmin(admin.ModelAdmin):
    list_display = ['name', 'province', 'state']


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',  'province', 'state']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',  'weight', 'height']
