from django.db import models


class TestModel(models.Model):
    test_string = models.CharField(max_length=20)
    test_datetime = models.DateTimeField("date")


