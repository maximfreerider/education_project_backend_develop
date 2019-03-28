from django.contrib import admin
from polls.models import User, Package, Mode_Of_Study, CustomUser


class AdminCustomerUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    fields = ('first_name', 'last_name')


admin.site.register(CustomUser, AdminCustomerUser)


class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    fields = ('first_name', 'last_name', 'email', 'date_of_birth')


admin.site.register(User, AdminUser)


class PackageAdmin(admin.ModelAdmin):
    list_display = ('name_of_package', 'price', 'lenght_discription', 'short_discription')
    fields = ('name_of_package', 'price', 'lenght_discription', 'short_discription')


admin.site.register(Package, PackageAdmin)


class ModeOfStudyAdmin(admin.ModelAdmin):
    list_display = ('name_of_mos', 'description', 'image_for_presentation', 'text_for_read')


admin.site.register(Mode_Of_Study, ModeOfStudyAdmin)