from django.db import models
from django.core.exceptions import ValidationError


def validate_name(value):
    if not all(char.isdigit() or char.lower() in ['a', 'b', 'c', 'd', 'e', 'f'] for char in value):
        raise ValidationError('Имя должно содержать только цифры от 0 до 9 и только буквы от a до f')


class Player(models.Model):
    name = models.CharField(max_length=54, default="", unique=True, validators=[validate_name])
    email = models.EmailField(max_length=54, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Game(models.Model):
    name = models.CharField(max_length=254, default="")
    players = models.ManyToManyField(Player, blank=True, related_name='player_games')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
