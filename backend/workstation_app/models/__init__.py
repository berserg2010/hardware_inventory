from .workstation import Workstation
from .base_board import BaseBoard
from .disk_drive import DiskDrive
from .network_adapter import NetworkAdapter
from .operating_system import OperatingSystem
from .physical_memory import PhysicalMemory
from .processor import Processor
from .video_controller import VideoController

list_class_models = (
    Workstation,
    BaseBoard,
    DiskDrive,
    NetworkAdapter,
    OperatingSystem,
    PhysicalMemory,
    Processor,
    VideoController,
)

list_models = (
    "BaseBoard",
    "DiskDrive",
    "NetworkAdapter",
    "OperatingSystem",
    "PhysicalMemory",
    "Processor",
    "VideoController",
)
