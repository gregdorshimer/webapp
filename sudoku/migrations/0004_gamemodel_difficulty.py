# Generated by Django 5.1 on 2024-11-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0003_gamemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemodel',
            name='difficulty',
            field=models.CharField(default='none', max_length=16),
        ),
    ]