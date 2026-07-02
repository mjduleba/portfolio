from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    github_url = models.URLField()
    linkedin_url = models.URLField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
