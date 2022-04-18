from django.contrib import admin
from .models import Client , Chair , Meal
# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name','price' , 'info')

class ClientAdmin(admin.ModelAdmin):
    filter_horizontal = ('meals','chair',)

admin.site.register(Meal , MealAdmin)
admin.site.register(Client)
admin.site.register(Chair)