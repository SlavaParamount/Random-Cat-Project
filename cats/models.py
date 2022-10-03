from django.db import models

class Pic(models.Model):
    uri = models.URLField("ссылка")
