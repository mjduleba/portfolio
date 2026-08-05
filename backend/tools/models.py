from django.contrib.postgres.fields import ArrayField
from django.db import models


class Tool(models.Model):
    class Category(models.TextChoices):
        DEMO = 'Demo'
        TOOL = 'Tool'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.TextField()
    url = models.URLField(blank=True, default="")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class SkillAgentEntry(models.Model):
    class Kind(models.TextChoices):
        SKILL = 'Skill'
        AGENT = 'Agent'

    tool = models.ForeignKey(Tool, related_name="skill_agent_entries", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=20, choices=Kind.choices)
    description = models.TextField()
    tags = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    video_url = models.URLField(blank=True, default="")
    image_url = models.URLField(blank=True, default="")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name
