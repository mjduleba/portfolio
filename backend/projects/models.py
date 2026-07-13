from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = ArrayField(models.CharField(max_length=100))
    github_url = models.URLField()
    demo_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
