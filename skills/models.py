from django.db import models


class Skill(models.Model):
    class Category(models.TextChoices):
        LANGUAGES = 'Languages & Querying'
        FRAMEWORKS = 'Frameworks, Libraries & Tools'
        CLOUD = 'Cloud & Infrastructure'
        CONCEPTS = 'Technical Concepts'

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=Category.choices)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f"{self.name} ({self.category})"
