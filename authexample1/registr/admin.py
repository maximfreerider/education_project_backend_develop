from django.contrib import admin
from .models import CustomUser
from .models import Package


class AdminCustomUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'password')
    fields = ('first_name', 'last_name', 'username', 'photo', 'bio', 'packages', 'email', 'password')


admin.site.register(CustomUser, AdminCustomUser)


class AdminPackage(admin.ModelAdmin):
    list_display = ('name_of_package',)
    fields = ('name_of_package',)


admin.site.register(Package, AdminPackage)
