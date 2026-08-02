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
