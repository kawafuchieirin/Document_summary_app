# crossword_app/models.py
from django.db import models

class AcrossClue(models.Model):
    clue_text = models.CharField(max_length=255)

    def __str__(self):
        return self.clue_text

class DownClue(models.Model):
    clue_text = models.CharField(max_length=255)

    def __str__(self):
        return self.clue_text
