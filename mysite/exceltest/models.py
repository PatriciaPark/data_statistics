from django.db import models

class SampleModel(models.Model): Name = models.CharField(
    max_length = 10,
    null = False
)
Number = models.IntegerField(null = True)
Item = models.CharField(max_length = 10, null = True)