from django.contrib import admin
from . models import Dojo, Operator, Player

# Register your models here.
admin.site.register(Dojo)
admin.site.register(Operator)
admin.site.register(Player)
