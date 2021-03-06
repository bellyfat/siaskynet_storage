import uuid

from django.db import models
from django.conf import settings

from storage.validators import validate_link

# Create your models here.
class File(models.Model):
    id = models.CharField(
        primary_key=True, max_length=40, default=uuid.uuid4, unique=True, editable=False
    )
    file = models.TextField()
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="files", on_delete=models.CASCADE
    )
    public = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def generate_link(self):
        url = self.file.split("//")[1]
        return f"https://siasky.net/{url}"

    class Meta:
        ordering = ["-updated", "name"]
