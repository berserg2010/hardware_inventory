from django.db import models

from inventory.models import InventoryNumberMixin


class MemoryMixin(models.Model):

    size = models.PositiveIntegerField(verbose_name="Размер памяти")
    form_factor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Форм-фактор")

    @classmethod
    def _list_fields(cls):
        return (
            "size",
            "form_factor",
        )

    class Meta:
        abstract = True


class NetworkMixin(models.Model):

    mac_address = models.CharField(max_length=12, null=True, blank=True, verbose_name="MAC адрес")

    @classmethod
    def _list_fields(cls):
        return (
            "mac_address",
        )

    class Meta:
        abstract = True


class BaseHardware(InventoryNumberMixin):

    manufacturer = models.CharField(max_length=255, null=True, blank=True, verbose_name="Производитель")
    product_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Наименование")
    version = models.CharField(max_length=255, null=True, blank=True, verbose_name="Версия")

    @classmethod
    def _list_fields(cls):
        return (
            *InventoryNumberMixin._list_fields(),
            "manufacturer",
            "product_name",
            "version",
        )

    class Meta:
        abstract = True


class Motherboard(BaseHardware):

    socket = models.CharField(max_length=255, null=True, blank=True, verbose_name="Сокет")
    chipset = models.CharField(max_length=255, null=True, blank=True, verbose_name="Чипсет")
    memory = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип памяти")
    graphic = models.CharField(max_length=255, null=True, blank=True, verbose_name="Графический адаптер")
    form_factor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Форм-фактор")

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            "socket",
            "chipset",
            "memory",
            "graphic",
            "form_factor",
        )

    class Meta:
        ordering = ["-created"]
        verbose_name = "01 | Материнская плата"
        verbose_name_plural = "01 | Материнские платы"


class Microprocessor(BaseHardware):

    core_count = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Колличество ядер")
    lithography = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Техпроцесс")
    frequency = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Частота")

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            "core_count",
            "lithography",
            "frequency",
        )

    class Meta:
        ordering = ["-created"]
        verbose_name = "02 | Процессор"
        verbose_name_plural = "02 | Процессоры"


class Memory(BaseHardware, MemoryMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *MemoryMixin._list_fields(),
        )

    class Meta:
        ordering = ["-created"]
        verbose_name = "03 | Оперативная память"
        verbose_name_plural = "03 | Оперативная память"


class Storage(BaseHardware, MemoryMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *MemoryMixin._list_fields(),
        )

    class Meta:
        ordering = ["-created"]
        verbose_name = "04 | Жесткий диск"
        verbose_name_plural = "04 | Жесткие диски"


class VideoCard(BaseHardware):

    interface = models.CharField(max_length=255, null=True, blank=True, verbose_name="Интерфейс")

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            "interface",
        )

    class Meta:
        ordering = ["-created"]
        verbose_name = "05 | Видеокарта"
        verbose_name_plural = "05 | Видеокарты"


class Monitor(BaseHardware):

    panel_size = models.CharField(max_length=255, null=True, blank=True, verbose_name="Размер экрана")
    panel_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="Тип экрана")

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            "panel_size",
            "panel_type",
        )

    class Meta:
        ordering = ["-created"]
        verbose_name = "06 | Монитор"
        verbose_name_plural = "06 | Мониторы"


class PowerSupply(BaseHardware):

    class Meta:
        ordering = ["-created"]
        verbose_name = "07 | Блок питания"
        verbose_name_plural = "07 | Блоки питания"


class OpticalDiscDrive(BaseHardware):

    class Meta:
        ordering = ["-created"]
        verbose_name = "08 | Привод оптических дисков"
        verbose_name_plural = "08 | Приводы оптических дисков"


class NetworkCard(BaseHardware, NetworkMixin):

    @classmethod
    def _list_fields(cls):
        return (
            *BaseHardware._list_fields(),
            *NetworkMixin._list_fields(),
        )

    class Meta:
        ordering = ["-created"]
        verbose_name = "09 | Сетевая карта"
        verbose_name_plural = "09 | Сетевые карты"
