from django.contrib import admin

from .models import TestModel
from .models import GameModel
from .models import Flagged

admin.site.register(TestModel)
admin.site.register(GameModel)
admin.site.register(Flagged)