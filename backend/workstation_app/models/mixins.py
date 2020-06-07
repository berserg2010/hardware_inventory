from django.db import models


class InventoryNumberMixin:
    inventory_number = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)


class MemoryMixin:
    size = models.PositiveIntegerField()
    form_factor = models.CharField(max_length=255)


class NetworkMixin:
    mac_address = models.CharField(max_length=12)
