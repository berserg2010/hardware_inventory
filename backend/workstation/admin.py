from django.contrib import admin

from .models import (
    Workstation,
)


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
    list_display = (
        *Workstation._list_fields(),
        *CustomListHardwareModelAdmin.list_display,
    )
