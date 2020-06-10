from django.db import models

from hardware.models import BaseHardware, NetworkMixin


class Router(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )

    class Meta:
        verbose_name = "01 | Маршрутизатор"
        verbose_name_plural = "01 | Маршрутизаторы"


class Switсh(BaseHardware):

    class Meta:
        verbose_name = "02 | Комутатор"
        verbose_name_plural = "02 | Комутаторы"


class MFU(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )

    class Meta:
        verbose_name = "03 | МФУ"
        verbose_name_plural = "03 | МФУ"


class Printer(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )

    class Meta:
        verbose_name = "04 | Принтер"
        verbose_name_plural = "04 | Принтеры"


class Scanner(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )

    class Meta:
        verbose_name = "05 | Сканер"
        verbose_name_plural = "05 | Сканеры"
