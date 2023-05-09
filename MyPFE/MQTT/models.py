from django.conf import settings
from django.db import models
from django.utils import timezone
from map.models import nodes

class Post(models.Model):
    temperature = models.BigIntegerField()
    humidity = models.BigIntegerField()
    published_date = models.DateTimeField(blank=True, null=True)
    po = models.ForeignKey(nodes, on_delete=models.CASCADE, null=True, blank=True,related_name='%(class)s_related')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity}, Published: {self.published_date}'