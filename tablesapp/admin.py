from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.


class ViewAdmin(ImportExportModelAdmin):
    pass


admin.site.register(modelValues, ViewAdmin)
