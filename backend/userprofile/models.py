from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    github_url = models.URLField()
    linkedin_url = models.URLField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Hobby(models.Model):
    profile = models.ForeignKey(UserProfile, related_name="hobbies", on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    icon_key = models.SlugField(max_length=50)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.label
