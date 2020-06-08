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

    socket = models.CharField(max_length=255, null=True, blank=True)
    chipset = models.CharField(max_length=255, null=True, blank=True)
    memory = models.CharField(max_length=255, null=True, blank=True)
    graphic = models.CharField(max_length=255, null=True, blank=True)
    form_factor = models.CharField(max_length=255, null=True, blank=True)


class Microprocessor(BaseWorkstationHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            "core_count",
            "lithography",
            "frequency",
        )

    core_count = models.PositiveSmallIntegerField(null=True, blank=True)
    lithography = models.PositiveSmallIntegerField(null=True, blank=True)
    frequency = models.PositiveSmallIntegerField(null=True, blank=True)


class VideoCard(BaseWorkstationHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            "interface",
        )

    interface = models.CharField(max_length=255, null=True, blank=True)


class Monitor(BaseWorkstationHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            "panel_size",
            "panel_type",
        )

    panel_size = models.CharField(max_length=255, null=True, blank=True)
    panel_type = models.CharField(max_length=255, null=True, blank=True)


class PowerSupply(BaseWorkstationHardware):

    pass

    # @classmethod
    # def _list_fields(cls):
    #     return (
    #         *BaseWorkstationHardware._list_fields(),
    #     )


class OpticalDiscDrive(BaseWorkstationHardware):

    pass

    # @classmethod
    # def _list_fields(cls):
    #     return (
    #         *BaseWorkstationHardware._list_fields(),
    #     )


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


class NetworkCard(BaseWorkstationHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseWorkstationHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )
