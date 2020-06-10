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
from .models import Workstation


class CustomListHardwareModelAdmin(admin.ModelAdmin):

    list_display = [
        "get_list_motherboards",
        "get_list_microprocessors",
        "get_list_memory",
        "get_list_storage",
        "get_list_videocards",
        "get_list_monitors",
        "get_list_powersupply",
        "get_list_opticaldiscdrive",
        "get_list_networkcards",
    ]
    list_filter = ["inventory_number", "description"]
    list_select_related = False
    preserve_filters = False
    save_on_top = True
    search_fields = (
        "motherboard__description",
        "microprocessor__description",
        "memory__description",
        "storage__description",
        "video_card__description",
        "monitor__description",
        "power_supply__description",
        "optical_disc_drive__description",
        "network_card__description",
    )
    readonly_fields = ("created", "changed")


    def get_list_motherboards(self, obj):
        instance = obj.motherboard.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_motherboards.short_description = "Материнские платы"


    def get_list_microprocessors(self, obj):
        instance = obj.microprocessor.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_microprocessors.short_description = "Процессоры"


    def get_list_memory(self, obj):
        instance = obj.memory.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_memory.short_description = "Оперативная память"


    def get_list_storage(self, obj):
        instance = obj.storage.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_storage.short_description = "Жесткие диски"


    def get_list_videocards(self, obj):
        instance = obj.video_card.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_videocards.short_description = "Видеокарты"


    def get_list_monitors(self, obj):
        instance = obj.monitor.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_monitors.short_description = "Мониторы"


    def get_list_networkcards(self, obj):
        instance = obj.network_card.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_networkcards.short_description = "Сетевые карты"


    def get_list_powersupply(self, obj):
        instance = obj.power_supply.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_powersupply.short_description = "Блоки питания"


    def get_list_opticaldiscdrive(self, obj):
        instance = obj.optical_disc_drive.filter()
        if instance.exists():
            return [*instance]
        else:
            return []
    get_list_opticaldiscdrive.short_description = "Оптические приводы"


@admin.register(Workstation)
class WorkstationAdmin(CustomListHardwareModelAdmin):

    list_display = (
        *Workstation._list_fields(),
        *CustomListHardwareModelAdmin.list_display,
    )
    fields = Workstation._list_fields()
    radio_fields = {"type": admin.HORIZONTAL}
    inlines = [
        MotherboardInline,
        MicroprocessorInline,
        MemoryInline,
        StorageInline,
        VideoCardInline,
        MonitorInline,
        PowerSupplyInline,
        OpticalDiscDriveInline,
        NetworkCardInline,
    ]
