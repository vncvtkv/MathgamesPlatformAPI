from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    """
    Model for Players
    There are two types of players: human and AI.
    Player is connected with User
    """

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
    """
    Model for game include:
    1. board - state of plyaing chess-field
    2. current player - player who makes current move
    3. opponent - player who wait in this moment
    4. winner - by default this field is null,
    then we have a winner game is finished.
    """

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
    """
    Model for Moves
    This model creating for looking at
    moves of players - (from_col, from_row) -> (to_col, to_row)
    """

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    from_row = models.IntegerField()
    from_col = models.IntegerField()
    to_row = models.IntegerField()
    to_col = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
