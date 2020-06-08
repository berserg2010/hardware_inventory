from django.db import models

from hardware.models import BaseHardware, NetworkMixin


class Router(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )


class MFU(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )

    class Meta:
        verbose_name = "MFU"


class Printer(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )


class Scanner(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )


class Switсh(BaseHardware):

    class Meta:
        verbose_name_plural = "Switches"
