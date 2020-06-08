from django.contrib import admin

from .models import (
    Router,
    Printer,
    MFU,
    Scanner,
    Switсh,
)


@admin.register(Router)
class RouterAdmin(admin.ModelAdmin):
    list_display = Router._list_fields()


@admin.register(MFU)
class MFUAdmin(admin.ModelAdmin):
    list_display = MFU._list_fields()


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = Printer._list_fields()


@admin.register(Scanner)
class ScannerAdmin(admin.ModelAdmin):
    list_display = Scanner._list_fields()


@admin.register(Switсh)
class SwitсhAdmin(admin.ModelAdmin):
    list_display = Switсh._list_fields()
