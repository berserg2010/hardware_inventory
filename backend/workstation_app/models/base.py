from django.db import models

from .mixins import InventoryNumberMixin
from .workstation import Workstation


class BaseHardware(models.Model, InventoryNumberMixin):
    manufacturer = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)

    class Meta:
        abstract = True


class BaseWorkstationHardware(BaseHardware):
    workstation = models.ManyToManyField(
        Workstation,
        related_name='%(class)s_workstation_set',
        related_query_name='%(class)ss_workstation',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
