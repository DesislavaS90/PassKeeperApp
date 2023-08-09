from django.db import models


class Facts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Advices(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Fun(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return 'fun subtitles'
