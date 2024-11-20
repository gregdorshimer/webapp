from django.db import models


class TestModel(models.Model):
    test_string = models.CharField(max_length=20)
    test_datetime = models.DateTimeField("date")
    test_field1 = models.CharField(max_length=20,default="default") # 'default=' defines the value that is initialized for rows that existed before this field was migrated

    def __str__(self):
        return self.test_string
