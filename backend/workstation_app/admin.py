from django.contrib import admin

from .models import list_class_models


@admin.register(*list_class_models)
class WorkstationAdmin(admin.ModelAdmin):
    pass
