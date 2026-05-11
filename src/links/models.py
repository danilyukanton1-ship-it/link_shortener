from django.db import models
from core.models import BaseModel


class Link(BaseModel):
    original_url = models.URLField()
    short_code = models.CharField(
        max_length=10,
        unique=True,
    )
    clicks = models.PositiveIntegerField(default=0)
