from django.db import models


class InventoryNumberMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "inventory_number",
            "description",
            "created",
        )

    inventory_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    description = models.CharField(max_length=255, null=True, blank=False, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        if self.inventory_number:
            inventory_number = f"{self.inventory_number} | "
        else:
            inventory_number = ""

        return f"{inventory_number}{self.description} | {self.created.date()}"

    class Meta:
        abstract = True
