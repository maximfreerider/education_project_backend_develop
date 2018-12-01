from django.contrib import admin
from polls.models import User, Package


class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'email')


admin.site.register(User, AdminUser)


class PackageAdmin(admin.ModelAdmin):
    list_display = ('mode_of_study_id', 'users', 'name_of_package', 'price', 'lenght_discription', 'short_discription')

    def packages(self, obj):
        return "\n".join([])
admin.site.register(Package, PackageAdmin)
