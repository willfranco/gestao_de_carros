from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('models', 'brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin) #Pede 2 parametros, qual tabela que é (Model) e as configs de CarAdmin, que acabamos de criar
admin.site.register(Brand, BrandAdmin)