from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    reply = models.TextField(blank=True, null=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return self.name
