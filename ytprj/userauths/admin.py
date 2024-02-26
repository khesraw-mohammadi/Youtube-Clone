from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin):
    pass


admin.site.register(User, UserAdmin)
