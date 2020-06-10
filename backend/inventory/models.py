from django.db import models
from django.utils import timezone


class InventoryNumberMixin(models.Model):

    inventory_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    description = models.CharField(max_length=255, null=True, blank=False, verbose_name="Описание")
    received = models.DateField(default=timezone.now, verbose_name="Поступило")
    created = models.DateField(auto_now_add=True, verbose_name="Запись создана")
    changed = models.DateField(auto_now=True, verbose_name="Запись изменена")

    @classmethod
    def _list_fields(cls):
        return (
            "inventory_number",
            "description",
            "received",
            "created",
            "changed",
        )

    def __str__(self):

        if self.inventory_number:
            inventory_number = f"{self.inventory_number} | "
        else:
            inventory_number = ""

        return f"{inventory_number}{self.description} | {self.received}"

    class Meta:
        abstract = True
