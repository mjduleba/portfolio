from django.contrib.postgres.fields import ArrayField
from django.db import models


class Tool(models.Model):
    class Category(models.TextChoices):
        DEMO = 'Demo'
        TOOL = 'Tool'
        GUIDE = 'Guide'

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


class GuidePattern(models.Model):
    tool = models.ForeignKey(Tool, related_name="guide_patterns", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    how_it_works = models.TextField()
    diagram_svg = models.TextField(blank=True, default="")
    recognition_signals = ArrayField(models.CharField(max_length=300), default=list, blank=True)
    code_solution = models.TextField()
    code_language = models.CharField(max_length=30, default="python")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class GuideExampleProblem(models.Model):
    pattern = models.ForeignKey(GuidePattern, related_name="example_problems", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, default="")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title
