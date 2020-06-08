from django.db import models

from .mixins import InventoryNumberMixin


workstation_enum = [
    ("PC", "PC"),
    ("NB", "Notebook"),
]

class Workstation(InventoryNumberMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *InventoryNumberMixin._list_fields(),
            "type",
        )

    type = models.CharField(
        max_length=2,
        choices=workstation_enum,
        default="PC",
    )

    def __str__(self):
        return f"{self.inventory_number} {self.type} {self.created.date()}"


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

    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    version = models.CharField(max_length=255, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class BaseWorkstationHardware(BaseHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
        )

    workstations = models.ManyToManyField(
        "Workstation",
        related_name='%(class)s_workstation_set',
        related_query_name='%(class)ss_workstation',
        blank=True,
        default=None,
    )

    class Meta:
        abstract = True
