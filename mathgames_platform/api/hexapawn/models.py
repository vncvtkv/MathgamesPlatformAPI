from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    AI = 'ai'
    HUMAN = 'human'
    PLAYER_TYPES = [
        (AI, 'AI'),
        (HUMAN, 'Human'),
    ]
    
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        null=True,
        blank=True,
        related_name='player_profile'
    )
    player_type = models.CharField(max_length=10, choices=PLAYER_TYPES)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name or f"Player-{self.id}"
    

class Game(models.Model):
    board = models.JSONField(default=list)
    current_player = models.ForeignKey(
        Player, 
        on_delete=models.CASCADE, 
        related_name='current_games'
    )
    opponent = models.ForeignKey(
        Player, 
        on_delete=models.CASCADE, 
        related_name='opponent_games'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='games'
    )
    winner = models.ForeignKey(
        Player, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    from_row = models.IntegerField()  # 0-2
    from_col = models.IntegerField()  # 0-2
    to_row = models.IntegerField()    # 0-2
    to_col = models.IntegerField()    # 0-2
    created_at = models.DateTimeField(auto_now_add=True)