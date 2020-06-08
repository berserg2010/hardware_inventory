from django.db import models

from .base import BaseWorkstationHardware
from .mixins import MemoryMixin, NetworkMixin


class Motherboard(BaseWorkstationHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
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


class Microprocessor(BaseWorkstationHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            "core_count",
            "lithography",
            "frequency",
        )

    core_count = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Колличество ядер")
    lithography = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Техпроцесс")
    frequency = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Частота")


class VideoCard(BaseWorkstationHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            "interface",
        )

    interface = models.CharField(max_length=255, null=True, blank=True, verbose_name="Интерфейс")

    class Meta:
        verbose_name_plural = "Video Cards"


class Monitor(BaseWorkstationHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            "panel_size",
            "panel_type",
        )

    panel_size = models.CharField(max_length=255, null=True, blank=True, verbose_name="Размер экрана")
    panel_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип экрана")


class PowerSupply(BaseWorkstationHardware):

    class Meta:
        verbose_name_plural = "Power Supply"


class OpticalDiscDrive(BaseWorkstationHardware):

    class Meta:
        verbose_name_plural = "Optical Disc Drives"


class Storage(BaseWorkstationHardware, MemoryMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            *MemoryMixin._list_fields(),
        )


class Memory(BaseWorkstationHardware, MemoryMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            *MemoryMixin._list_fields(),
        )

    class Meta:
        verbose_name_plural = "Memory"


class NetworkCard(BaseWorkstationHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )

    class Meta:
        verbose_name_plural = "Network Cards"
