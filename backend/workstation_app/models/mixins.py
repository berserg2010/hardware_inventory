from django.db import models


class InventoryNumberMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "inventory_number",
            "created",
            "description",
        )

    inventory_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        if self.inventory_number:
            inventory_number = f"{self.inventory_number} | "
        else:
            inventory_number = ""

        return f"{inventory_number}{self.description} | {self.created.date()}"

    class Meta:
        abstract = True


class MemoryMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "size",
            "form_factor",
        )

    size = models.PositiveIntegerField(verbose_name="Размер памяти")
    form_factor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Форм-фактор")

    class Meta:
        abstract = True


class NetworkMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "mac_address",
        )

    mac_address = models.CharField(max_length=12, null=True, blank=True, verbose_name="MAC адрес")

    class Meta:
        abstract = True
