from django.db import models


class TestModel(models.Model):
    test_string = models.CharField(max_length=20)
    test_datetime = models.DateTimeField("date")

    def __str__(self):
        return self.test_string


