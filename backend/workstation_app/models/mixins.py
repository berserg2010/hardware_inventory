from django.db import models


class InventoryNumberMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "inventory_number",
            "created",
            "description",
        )

    inventory_number = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class MemoryMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "size",
            "form_factor",
        )

    size = models.PositiveIntegerField()
    form_factor = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class NetworkMixin(models.Model):

    @classmethod
    def _list_fields(cls):
        return (
            "mac_address",
        )

    mac_address = models.CharField(max_length=12, null=True, blank=True)

    class Meta:
        abstract = True
