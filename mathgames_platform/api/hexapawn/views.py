from rest_framework import generics, status
from rest_framework.response import Response
from .models import Game, Player, Move
from .serializers import GameSerializer, MoveSerializer
from rest_framework import serializers
import random
from .game_logic import HexapawnEngine, format_board_to_text

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
            ['W', 'W', 'W'],
            ['.', '.', '.'],
            ['B', 'B', 'B']
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

    def post(self, request, *args, **kwargs):
        game = Game.objects.get(pk=self.kwargs['game_id'])
        player = game.current_player

        if game.winner:
            return Response({"error": "Игра уже завершена"}, status=400)
        
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        # Проверяем ход (здесь должна быть валидация правил Hexapawn)
        from_row = serializer.validated_data['from_row']
        from_col = serializer.validated_data['from_col']
        to_row = serializer.validated_data['to_row']
        to_col = serializer.validated_data['to_col']

        if not all(0 <= coord <= 2 for coord in [from_row, from_col, to_row, to_col]):
            return Response({"error": "Координаты должны быть от 0 до 2"}, status=400)
        
        error = HexapawnEngine.validate_move(game.board, from_row, from_col, to_row, to_col, player)
        if error:
            return Response({"error": error}, status=400)
        
        # Обновляем доску
        board = game.board
        piece = board[from_row][from_col]
        board[from_row][from_col] = '.'
        board[to_row][to_col] = piece
        game.board = board

        # Проверяем победу
        winner = HexapawnEngine.check_winner(board, game.opponent)
        if winner:
            game.winner = player
            game.save()
            return Response({"status": f"Победил {game.winner.name}!", "board": format_board_to_text(board)})
    
        # Сохраняем ход
        Move.objects.create(
            game=game,
            player=player,
            from_row=from_row,
            from_col=from_col,
            to_row=to_row,
            to_col=to_col
        )

        # Ход ИИ (если нужно)
        if game.opponent.player_type == 'ai' and not winner:
            HexapawnEngine.make_ai_move(game)

        return Response({"status": "Ход принят", "board": format_board_to_text(board)})