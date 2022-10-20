from django.db import models


class Difficulty(models.Model):
    name = models.CharField(max_length=7, null=True)

    def __str__(self):
        return self.name
        

class Problem(models.Model):
    difficulty  = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    name        = models.CharField(max_length=256, null=True)
    topic       = models.CharField(max_length=256, null=True)
    add_date    = models.DateTimeField(auto_now_add=True)
    link        = models.URLField(max_length=256, unique=True, blank=True)
    note        = models.TextField(null=True)
    source_code = models.FileField(upload_to='source_code/', null=True, default=None)

    def __str__(self):
        return self.name


class Links(models.Model):
    name = models.CharField(max_length=256, null=True)
    url  = models.URLField(max_length=256, unique=True, blank=True)

    def __str__(self):
        return self.name
