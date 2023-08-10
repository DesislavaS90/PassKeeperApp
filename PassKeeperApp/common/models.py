from django.db import models


class Facts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Facts'


class Advices(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Advices'


class Fun(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return 'fun subtitles'

    class Meta:
        verbose_name_plural = 'Fun'
