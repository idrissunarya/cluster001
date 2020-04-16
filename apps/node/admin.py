from django.contrib import admin
from .models import Departement, Member

class DepartementModelAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Departement

admin.site.register(Departement, DepartementModelAdmin)


class MemberModelAdmin(admin.ModelAdmin):
    list_display = ['member_id', 'first_name', 'last_name', 'birthday', 'email', 'phone', 'address', 'age']

    class Meta:
        model = Member

admin.site.register(Member, MemberModelAdmin)
