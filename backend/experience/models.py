from django.db import models
from django.contrib.postgres.fields import ArrayField


class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_icon_key = models.SlugField(max_length=50, blank=True, default="")
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"


class ExperienceBullet(models.Model):
    experience = models.ForeignKey(Experience, related_name="bullets", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    tags = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.text[:50]