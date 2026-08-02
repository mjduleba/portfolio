from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = ArrayField(models.CharField(max_length=100))
    github_url = models.URLField()
    demo_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, default="")
    image_url = models.URLField(blank=True, default="")
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ProjectBullet(models.Model):
    project = models.ForeignKey(Project, related_name="bullets", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    tags = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.text[:50]
