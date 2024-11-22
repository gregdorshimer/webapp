from django.contrib import admin

from .models import TestModel
from .models import GameModel

admin.site.register(TestModel)
admin.site.register(GameModel)