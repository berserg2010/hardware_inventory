from django.db import models

from .base import BaseWorkstationHardware
from .mixins import MemoryMixin, NetworkMixin


class Motherboard(BaseWorkstationHardware):
    socket = models.CharField(max_length=255)
    chipset = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    graphic = models.CharField(max_length=255)
    form_factor = models.CharField(max_length=255)


class Microprocessor(BaseWorkstationHardware):
    core_count = models.PositiveSmallIntegerField()
    lithography = models.PositiveSmallIntegerField()
    frequency = models.PositiveSmallIntegerField()


class VideoCard(BaseWorkstationHardware):
    interface = models.CharField(max_length=255)


class Monitor(BaseWorkstationHardware):
    panel_size = models.CharField(max_length=255)
    panel_type = models.CharField(max_length=255)


class PowerSupply(BaseWorkstationHardware):
    pass


class OpticalDiscDrive(BaseWorkstationHardware):
    pass


class Storage(BaseWorkstationHardware, MemoryMixin):
    pass


class Memory(BaseWorkstationHardware, MemoryMixin):
    pass


class NetworkCard(BaseWorkstationHardware, NetworkMixin):
    pass
