from django.db import models

from .base import BaseHardware
from .mixins import NetworkMixin


class Router(BaseHardware, NetworkMixin):
    pass


class MFU(BaseHardware, NetworkMixin):
    pass


class Printer(BaseHardware, NetworkMixin):
    pass


class Scanner(BaseHardware, NetworkMixin):
    pass


class Switсh(BaseHardware):
    pass
