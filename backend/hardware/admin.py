from django.contrib import admin

from utils.utils import (
    MotherboardInline,
    MicroprocessorInline,
    MemoryInline,
    StorageInline,
    VideoCardInline,
    MonitorInline,
    PowerSupplyInline,
    OpticalDiscDriveInline,
    NetworkCardInline,
)
from .models import (
    Motherboard,
    Microprocessor,
    Memory,
    Storage,
    VideoCard,
    Monitor,
    PowerSupply,
    OpticalDiscDrive,
    NetworkCard,
)


class CustomListWorkstationsModelAdmin(admin.ModelAdmin):

    list_display_links = ("description",)
    list_display = ["get_list_workstations"]
    list_filter = ["manufacturer"]
    list_select_related = False
    preserve_filters = False
    save_on_top = True
    search_fields = ["inventory_number", "description"]
    exclude = ("workstation", )
    readonly_fields = ("created", "changed")


    def get_list_workstations(self, obj):
        instance = obj.workstation_set.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_workstations.short_description = "Рабочая станция"


@admin.register(Motherboard)
class MotherboardAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *Motherboard._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*Motherboard._list_fields(), )
    inlines = [MotherboardInline, ]


@admin.register(Microprocessor)
class MicroprocessorAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *Microprocessor._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*Microprocessor._list_fields(), )
    inlines = [MicroprocessorInline, ]


@admin.register(Memory)
class MemoryAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *Memory._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*Memory._list_fields(), )
    inlines = [MemoryInline, ]


@admin.register(Storage)
class StorageAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *Storage._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*Storage._list_fields(), )
    inlines = [StorageInline, ]


@admin.register(VideoCard)
class VideoCardAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *VideoCard._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*VideoCard._list_fields(), )
    inlines = [VideoCardInline, ]


@admin.register(Monitor)
class MonitorAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *Monitor._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*Monitor._list_fields(), )
    inlines = [MonitorInline, ]


@admin.register(PowerSupply)
class PowerSupplyAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *PowerSupply._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*PowerSupply._list_fields(), )
    inlines = [PowerSupplyInline, ]


@admin.register(OpticalDiscDrive)
class OpticalDiscDriveAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *OpticalDiscDrive._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*OpticalDiscDrive._list_fields(), )
    inlines = [OpticalDiscDriveInline, ]


@admin.register(NetworkCard)
class NetworkCardAdmin(CustomListWorkstationsModelAdmin):

    list_display = (
        *NetworkCard._list_fields(),
        *CustomListWorkstationsModelAdmin.list_display,
    )
    fields = (*NetworkCard._list_fields(), "workstations")
    inlines = [NetworkCardInline, ]
