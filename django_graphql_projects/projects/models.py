from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Project(models.Model):
    title = models.CharField(max_length=100)
    developers = models.ManyToManyField(Developer)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)