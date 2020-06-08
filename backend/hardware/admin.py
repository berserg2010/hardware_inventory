from django.contrib import admin

from .models import (
    Motherboard,
    Microprocessor,
    VideoCard,
    Monitor,
    PowerSupply,
    OpticalDiscDrive,
    Storage,
    Memory,
    NetworkCard,
)


class CustomListWorkstationsModelAdmin(admin.ModelAdmin):
    list_display = ["get_list_workstations"]

    def get_list_workstations(self, obj):
        instance = obj.workstations.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    get_list_workstations.short_description = "Установлено"


@admin.register(Motherboard)
class MotherboardAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*Motherboard._list_fields(), *CustomListWorkstationsModelAdmin.list_display)


@admin.register(Microprocessor)
class MicroprocessorAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*Microprocessor._list_fields(), *CustomListWorkstationsModelAdmin.list_display)


@admin.register(VideoCard)
class VideoCardAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*VideoCard._list_fields(), *CustomListWorkstationsModelAdmin.list_display)


@admin.register(Monitor)
class MonitorAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*Monitor._list_fields(), *CustomListWorkstationsModelAdmin.list_display)


@admin.register(PowerSupply)
class PowerSupplyAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*PowerSupply._list_fields(), *CustomListWorkstationsModelAdmin.list_display)


@admin.register(OpticalDiscDrive)
class OpticalDiscDriveAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*OpticalDiscDrive._list_fields(), *CustomListWorkstationsModelAdmin.list_display)


@admin.register(Storage)
class StorageAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*Storage._list_fields(), *CustomListWorkstationsModelAdmin.list_display)


@admin.register(Memory)
class MemoryAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*Memory._list_fields(), *CustomListWorkstationsModelAdmin.list_display)


@admin.register(NetworkCard)
class NetworkCardAdmin(CustomListWorkstationsModelAdmin):
    list_display = (*NetworkCard._list_fields(), *CustomListWorkstationsModelAdmin.list_display)
