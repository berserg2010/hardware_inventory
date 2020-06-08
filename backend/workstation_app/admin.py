from django.contrib import admin
from functools import wraps


from .models import (
    Workstation,
    Motherboard,
    Microprocessor,
    VideoCard,
    Monitor,
    PowerSupply,
    OpticalDiscDrive,
    Storage,
    Memory,
    NetworkCard,

    Router,
    Printer,
    MFU,
    Scanner,
    Switсh,
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


class CustomListHardwareModelAdmin(admin.ModelAdmin):

    list_display = [
        "get_list_motherboard",
        "get_list_microprocessor",
        "get_list_memory",
        "get_list_storage",
        "get_list_videocard",
        "get_list_monitor",
        "get_list_networkcard",
        "get_list_powersupply",
        "get_list_opticaldiscdrive",
    ]

    def get_list_memory(self, obj):
        instance = obj.memory_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    def get_list_microprocessor(self, obj):
        instance = obj.microprocessor_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    def get_list_monitor(self, obj):
        instance = obj.monitor_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    def get_list_motherboard(self, obj):
        instance = obj.motherboard_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    def get_list_networkcard(self, obj):
        instance = obj.networkcard_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    def get_list_opticaldiscdrive(self, obj):
        instance = obj.opticaldiscdrive_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    def get_list_powersupply(self, obj):
        instance = obj.powersupply_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    def get_list_storage(self, obj):
        instance = obj.storage_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []

    def get_list_videocard(self, obj):
        instance = obj.videocard_workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []


@admin.register(Workstation)
class WorkstationAdmin(CustomListHardwareModelAdmin):
    list_display = (*Workstation._list_fields(), *CustomListHardwareModelAdmin.list_display)


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


@admin.register(Router)
class RouterAdmin(admin.ModelAdmin):
    list_display = Router._list_fields()


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = Printer._list_fields()


@admin.register(MFU)
class MFUAdmin(admin.ModelAdmin):
    list_display = MFU._list_fields()


@admin.register(Scanner)
class ScannerAdmin(admin.ModelAdmin):
    list_display = Scanner._list_fields()


@admin.register(Switсh)
class SwitсhAdmin(admin.ModelAdmin):
    list_display = Switсh._list_fields()
