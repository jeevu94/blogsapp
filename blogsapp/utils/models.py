import uuid

from django.db import models

from .managers import BaseObjectManagerQuerySet


class BaseModel(models.Model):
    """
    Contains the last modified and the created fields, basically
    the base model for the entire app.
    """

    # unique id field
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    # time tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # custom manager
    objects = BaseObjectManagerQuerySet.as_manager()

    class Meta:
        ordering = ["-created_at"]
        abstract = True
