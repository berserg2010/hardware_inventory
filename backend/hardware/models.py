from django.db import models

from inventory.models import InventoryNumberMixin
from workstation.models import Workstation, WorkstationMixin


class MemoryMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "size",
            "form_factor",
        )

    size = models.PositiveIntegerField(verbose_name="Размер памяти")
    form_factor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Форм-фактор")

    class Meta:
        abstract = True


class NetworkMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "mac_address",
        )

    mac_address = models.CharField(max_length=12, null=True, blank=True, verbose_name="MAC адрес")

    class Meta:
        abstract = True


class BaseHardware(InventoryNumberMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *InventoryNumberMixin._list_fields(),
            "manufacturer",
            "product_name",
            "version",
            "serial_number",
        )

    manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name="Производитель")
    product_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Наименование")
    version = models.CharField(max_length=255, null=True, blank=True, verbose_name="Версия")
    serial_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="Серийный номер")

    class Meta:
        abstract = True


class Motherboard(BaseHardware, WorkstationMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            "socket",
            "chipset",
            "memory",
            "graphic",
            "form_factor",
        )

    socket = models.CharField(max_length=255, null=True, blank=True, verbose_name="Сокет")
    chipset = models.CharField(max_length=255, null=True, blank=True, verbose_name="Чипсет")
    memory = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип памяти")
    graphic = models.CharField(max_length=255, null=True, blank=True, verbose_name="Графический адаптер")
    form_factor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Форм-фактор")


class Microprocessor(BaseHardware, WorkstationMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            "core_count",
            "lithography",
            "frequency",
        )

    core_count = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Колличество ядер")
    lithography = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Техпроцесс")
    frequency = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Частота")


class Memory(BaseHardware, MemoryMixin, WorkstationMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *MemoryMixin._list_fields(),
        )

    class Meta:
        verbose_name_plural = "Memory"


class Storage(BaseHardware, MemoryMixin, WorkstationMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *MemoryMixin._list_fields(),
        )


class VideoCard(BaseHardware, WorkstationMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            "interface",
        )

    interface = models.CharField(max_length=255, null=True, blank=True, verbose_name="Интерфейс")

    class Meta:
        verbose_name_plural = "Video Cards"


class Monitor(BaseHardware, WorkstationMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            "panel_size",
            "panel_type",
        )

    panel_size = models.CharField(max_length=255, null=True, blank=True, verbose_name="Размер экрана")
    panel_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип экрана")


class PowerSupply(BaseHardware, WorkstationMixin):

    class Meta:
        verbose_name_plural = "Power Supply"


class OpticalDiscDrive(BaseHardware, WorkstationMixin):

    class Meta:
        verbose_name_plural = "Optical Disc Drives"


class NetworkCard(BaseHardware, NetworkMixin, WorkstationMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )

    class Meta:
        verbose_name_plural = "Network Cards"
