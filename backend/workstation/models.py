from django.db import models

from inventory.models import InventoryNumberMixin


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


class WorkstationMixin(models.Model):

    workstations = models.ManyToManyField(
        Workstation,
        related_name='%(class)s_workstation_set',
        related_query_name='%(class)ss_workstation',
        blank=True,
        default=None,
        verbose_name = "Рабочие станции"
    )

    class Meta:
        abstract = True
