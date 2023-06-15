from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    version = models.IntegerField()
    file_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
