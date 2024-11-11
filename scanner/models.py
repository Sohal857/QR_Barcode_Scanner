from django.db import models

class ScannedData(models.Model):
    data = models.CharField(max_length=100)  # To store scanned content
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for when it was scanned

    def __str__(self):
        return self.data