from rest_framework import serializers
from .models import Game, Player, Move


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'player_type', 'name',)


class GameSerializer(serializers.ModelSerializer):
    opponent_type = serializers.ChoiceField(
        choices=[('ai', 'AI'), ('human', 'Human')],
        write_only=True,
        default='ai'
    )
    current_player = serializers.StringRelatedField(read_only=True)
    opponent = serializers.StringRelatedField(read_only=True)
    winner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Game
        fields = (
            'id',
            'opponent_type',
            'current_player',
            'opponent',
            'board',
            'winner',
        )


class MoveSerializer(serializers.ModelSerializer):
    player = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Move
        fields = ('id', 'player', 'from_row', 'from_col', 'to_row', 'to_col',)
