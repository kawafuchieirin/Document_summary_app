from django.db import models

class Clue(models.Model):
    DIRECTION_CHOICES = (
        ('ACROSS', '横のカギ'),
        ('DOWN', '縦のカギ'),
    )
    number = models.IntegerField()
    direction = models.CharField(max_length=6, choices=DIRECTION_CHOICES)
    clue = models.TextField()
    answer = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.number} {self.get_direction_display()}: {self.clue}"
