from django.db import models
from django.contrib.postgres.fields import ArrayField

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    bullets = ArrayField(models.CharField(max_length=200), default=list)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.role} at {self.company}"