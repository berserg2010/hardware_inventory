from django.db import models

from .mixins import InventoryNumberMixin


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
        verbose_name="Тип"
    )




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
        verbose_name = "Рабочие станции"
    )

    class Meta:
        abstract = True
