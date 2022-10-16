from django.contrib import admin
from .models import Difficulty, Problem, Links

admin.site.register(Problem)
admin.site.register(Difficulty)
admin.site.register(Links)