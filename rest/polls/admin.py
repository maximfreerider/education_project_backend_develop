from django.contrib import admin
from polls.models import User, Package, Mode_Of_Study


class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


admin.site.register(User, AdminUser)


class PackageAdmin(admin.ModelAdmin):
    list_display = ('name_of_package', 'price', 'lenght_discription', 'short_discription')


admin.site.register(Package, PackageAdmin)


class ModeOfStudyAdmin(admin.ModelAdmin):
    list_display = ('name_of_mos', 'description', 'image_for_presentation', 'text_for_read')


admin.site.register(Mode_Of_Study, ModeOfStudyAdmin)