from django.db import models


workstation_enum = [
    ("PC", "PC"),
    ("NB", "Notebook"),
]

class Workstation(models.Model):
    type = models.CharField(
        max_length=2,
        choices=workstation_enum,
        default="PC",
    )