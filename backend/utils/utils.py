from django.contrib import admin

from workstation.models import (
    MotherboardRelationship,
    MicroprocessorRelationship,
    MemoryRelationship,
    StorageRelationship,
    VideoCardRelationship,
    MonitorRelationship,
    PowerSupplyRelationship,
    OpticalDiscDriveRelationship,
    NetworkCardRelationship,
)


def hardware_inline(model):
    def wrapped(cls):

        cls.model = model
        cls.extra = 0

        return cls
    return wrapped


@hardware_inline(MotherboardRelationship)
class MotherboardInline(admin.TabularInline):
    pass


@hardware_inline(MicroprocessorRelationship)
class MicroprocessorInline(admin.TabularInline):
    pass


@hardware_inline(MemoryRelationship)
class MemoryInline(admin.TabularInline):
    pass


@hardware_inline(StorageRelationship)
class StorageInline(admin.TabularInline):
    pass


@hardware_inline(VideoCardRelationship)
class VideoCardInline(admin.TabularInline):
    pass


@hardware_inline(MonitorRelationship)
class MonitorInline(admin.TabularInline):
    pass


@hardware_inline(PowerSupplyRelationship)
class PowerSupplyInline(admin.TabularInline):
    pass


@hardware_inline(OpticalDiscDriveRelationship)
class OpticalDiscDriveInline(admin.TabularInline):
    pass


@hardware_inline(NetworkCardRelationship)
class NetworkCardInline(admin.TabularInline):
    pass
