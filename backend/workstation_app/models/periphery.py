from django.db import models

from .base import BaseHardware
from .mixins import NetworkMixin


class Router(NetworkMixin, BaseHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *NetworkMixin._list_fields(),
            *BaseHardware._list_fields(),
        )


class MFU(NetworkMixin, BaseHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *NetworkMixin._list_fields(),
            *BaseHardware._list_fields(),
        )

    class Meta:
        verbose_name = "MFU"


class Printer(NetworkMixin, BaseHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *NetworkMixin._list_fields(),
            *BaseHardware._list_fields(),
        )


class Scanner(NetworkMixin, BaseHardware):

    @classmethod
    def _list_fields(cls):
        return (
            *NetworkMixin._list_fields(),
            *BaseHardware._list_fields(),
        )


class Switсh(BaseHardware):

    class Meta:
        verbose_name_plural = "Switches"
