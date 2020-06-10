from django.db import models
from django.utils import timezone

from inventory.models import InventoryNumberMixin
from hardware.models import (
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


workstation_enum = [
    ("PC", "PC"),
    ("NB", "Notebook"),
]


class Workstation(InventoryNumberMixin):

    type = models.CharField(
        max_length=2,
        choices=workstation_enum,
        default="PC",
        verbose_name="Тип"
    )
    motherboard = models.ManyToManyField(
        Motherboard,
        through="MotherboardRelationship",
        blank=True,
        default=None,
    )
    microprocessor = models.ManyToManyField(
        Microprocessor,
        through="MicroprocessorRelationship",
        blank=True,
        default=None,
    )
    memory = models.ManyToManyField(
        Memory,
        through="MemoryRelationship",
        blank=True,
        default=None,
        verbose_name="Оперативная память",
    )
    storage = models.ManyToManyField(
        Storage,
        through="StorageRelationship",
        blank=True,
        default=None,
    )
    video_card = models.ManyToManyField(
        VideoCard,
        through="VideoCardRelationship",
        blank=True,
        default=None,
    )
    monitor = models.ManyToManyField(
        Monitor,
        through="MonitorRelationship",
        blank=True,
        default=None,
    )
    power_supply = models.ManyToManyField(
        PowerSupply,
        through="PowerSupplyRelationship",
        blank=True,
        default=None,
    )
    optical_disc_drive = models.ManyToManyField(
        OpticalDiscDrive,
        through="OpticalDiscDriveRelationship",
        blank=True,
        default=None,
    )
    network_card = models.ManyToManyField(
        NetworkCard,
        through="NetworkCardRelationship",
        blank=True,
        default=None,
    )

    @classmethod
    def _list_fields(cls):
        return (
            *InventoryNumberMixin._list_fields(),
            "type",
        )

    class Meta:
        ordering = ("-created", )
        verbose_name = "01 | Рабочая станция"
        verbose_name_plural = "01 | Рабочие станции"


class WorkstationManyToManyMixin(models.Model):

    entered = models.DateField(default=timezone.now, verbose_name="Установлено")
    workstation = models.ForeignKey("Workstation", blank=True,
                                    default=None, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class MotherboardRelationship(WorkstationManyToManyMixin):
    motherboard = models.ForeignKey(Motherboard, blank=True,
                                    default=None, on_delete=models.CASCADE)


class MicroprocessorRelationship(WorkstationManyToManyMixin):
    microprocessor = models.ForeignKey(Microprocessor, blank=True,
                                       default=None, on_delete=models.CASCADE)


class MemoryRelationship(WorkstationManyToManyMixin):
    memory = models.ForeignKey(Memory, blank=True, default=None, on_delete=models.CASCADE)


class StorageRelationship(WorkstationManyToManyMixin):
    storage = models.ForeignKey(Storage, blank=True, default=None, on_delete=models.CASCADE)


class VideoCardRelationship(WorkstationManyToManyMixin):
    video_card = models.ForeignKey(VideoCard, blank=True, default=None, on_delete=models.CASCADE)


class MonitorRelationship(WorkstationManyToManyMixin):
    monitor = models.ForeignKey(Monitor, blank=True, default=None, on_delete=models.CASCADE)


class PowerSupplyRelationship(WorkstationManyToManyMixin):
    power_supply = models.ForeignKey(PowerSupply, blank=True, default=None, on_delete=models.CASCADE)


class OpticalDiscDriveRelationship(WorkstationManyToManyMixin):
    optical_disc_drive = models.ForeignKey(OpticalDiscDrive, blank=True, default=None, on_delete=models.CASCADE)


class NetworkCardRelationship(WorkstationManyToManyMixin):
    network_card = models.ForeignKey(NetworkCard, blank=True, default=None, on_delete=models.CASCADE)
