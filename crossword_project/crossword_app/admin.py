# crossword_app/admin.py
from django.contrib import admin
from .models import AcrossClue, DownClue

admin.site.register(AcrossClue)
admin.site.register(DownClue)
