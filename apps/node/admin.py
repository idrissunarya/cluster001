from django.contrib import admin
from .models import Departement

class DepartementModelAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Departement

admin.site.register(Departement, DepartementModelAdmin)
