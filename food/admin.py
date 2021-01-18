from django.contrib import admin
from .models import District, Restaurant, Dishes, Category, Saludinst, TypeOf
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(District, Restaurant, Dishes, Category, Saludinst, TypeOf)
class ViewAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
#admin.site.register(University)
#admin.site.register(Course)
#admin.site.register(Files)