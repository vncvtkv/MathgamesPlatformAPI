from rest_framework import generics, status
from rest_framework.response import Response
from .models import Game, Player, Move
from .serializers import GameSerializer, MoveSerializer
import random

# Create your views here.


class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        user = self.request.user
        
        # Определяем тип оппонента
        opponent_type = serializer.validated_data.pop('opponent_type', 'ai') 
        
        # Создаем или получаем игрока для текущего пользователя
        player, _ = Player.objects.get_or_create(
            user=user,
            defaults={
                'player_type': Player.HUMAN,
                'name': user.username
            }
        )
        
        # Создаем или получаем AI-игрока
        if opponent_type == 'ai':
            opponent, _ = Player.objects.get_or_create(
                name='Hexapawn AI',
                player_type=Player.AI,
                defaults={'user': None}
            )
        else:
            # Для игры против человека можно добавить логику выбора другого игрока
            opponent = player  # Временная заглушка

        # Инициализируем доску
        initial_board = [
            ['P', 'P', 'P'],
            ['.', '.', '.'],
            ['p', 'p', 'p']
        ]

        # Сохраняем игру через serializer
        serializer.save(
            created_by=user,
            current_player=player,
            opponent=opponent,
            board=initial_board
        )

class MoveView(generics.CreateAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

    def create(self, request, *args, **kwargs):
        game = Game.objects.get(pk=kwargs['game_id'])
        player = game.current_player

        # Проверяем ход (здесь должна быть валидация правил Hexapawn)
        from_pos = request.data.get('from_pos')
        to_pos = request.data.get('to_pos')

        # Обновляем доску
        board = game.board
        piece = board[int(from_pos[1])][ord(from_pos[0].upper()) - ord('A')]
        board[int(from_pos[1])][ord(from_pos[0].upper()) - ord('A')] = '.'
        board[int(to_pos[1])][ord(to_pos[0].upper()) - ord('A')] = piece
        game.board = board
        game.save()

        # Если противник — ИИ, он делает ход автоматически
        if game.opponent.player_type == 'ai':
            ai_move = self.make_ai_move(game)  # Реализуйте этот метод
            Move.objects.create(game=game, player=game.opponent, **ai_move)

        return Response({"status": "move accepted"}, status=status.HTTP_200_OK)

    def make_ai_move(self, game):
        # Простейший ИИ: случайный ход
        board = game.board
        possible_moves = []  # Здесь должна быть логика генерации ходов по правилам Hexapawn
        return random.choice(possible_moves)