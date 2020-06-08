from django.contrib import admin

from .models import (
    Workstation,
    Motherboard,
    Microprocessor,
    VideoCard,
)


@admin.register(Workstation)
class WorkstationAdmin(admin.ModelAdmin):
    list_display = Workstation._list_fields()


@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    list_display = Motherboard._list_fields()


@admin.register(Microprocessor)
class MicroprocessorAdmin(admin.ModelAdmin):
    list_display = Microprocessor._list_fields()


@admin.register(VideoCard)
class VideoCardAdmin(admin.ModelAdmin):
    list_display = VideoCard._list_fields()
