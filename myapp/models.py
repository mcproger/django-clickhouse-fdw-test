import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class MyAppModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, null=True, unique=True,
    )

    action = models.CharField(max_length=128)
    changed_at = models.DateTimeField(auto_created=True)
    object_id = models.PositiveIntegerField()

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
    )
    changed_object = GenericForeignKey('content_type', 'object_id')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
