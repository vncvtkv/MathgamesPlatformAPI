from rest_framework import generics, status
from rest_framework.response import Response
from .models import Game, Player, Move
from .serializers import GameSerializer, MoveSerializer
from .game_logic import HexapawnEngine, format_board_to_text


# Create your views here.


class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        """This method need to create new Game"""

        user = self.request.user

        # Define type of opponent
        opponent_type = serializer.validated_data.pop('opponent_type', 'ai')

        # Create player
        player, _ = Player.objects.get_or_create(
            user=user,
            defaults={
                'player_type': Player.HUMAN,
                'name': user.username
            }
        )

        # Create human opponent or AI - opponent
        if opponent_type == 'ai':
            opponent, _ = Player.objects.get_or_create(
                name='Hexapawn AI',
                player_type=Player.AI,
                defaults={'user': None}
            )
        else:
            # Later will fix this, for now opponent is yourself
            opponent = opponent, _ = Player.objects.get_or_create(
                name='EVIL player',
                player_type=Player.AI,
                defaults={'user': None}
            )

        # Initialize board
        initial_board = [
            ['W', 'W', 'W'],
            ['.', '.', '.'],
            ['B', 'B', 'B']
        ]

        # Create Game object using serializer
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
        """In post method we update game and make move"""

        game = Game.objects.get(pk=self.kwargs['game_id'])
        player = game.current_player

        if game.winner:
            return Response({"error": "The game is finished"},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        from_row = serializer.validated_data['from_row']
        from_col = serializer.validated_data['from_col']
        to_row = serializer.validated_data['to_row']
        to_col = serializer.validated_data['to_col']

        if not all(0 <= coord <= 2
                   for coord in [from_row, from_col, to_row, to_col]):
            return Response({"error": "Координаты должны быть от 0 до 2"},
                            status=status.HTTP_400_BAD_REQUEST)

        error = HexapawnEngine.validate_move(
            game.board,
            from_row,
            from_col,
            to_row,
            to_col,
            player
        )
        if error:
            return Response({"error": error},
                            status=status.HTTP_400_BAD_REQUEST)

        # Refresh board
        board = game.board
        piece = board[from_row][from_col]
        board[from_row][from_col] = '.'
        board[to_row][to_col] = piece
        game.board = board

        # Check for win
        winner = HexapawnEngine.check_winner(board, game.opponent)
        if winner:
            game.winner = player
            game.save()
            return Response({"status": f"Победил {game.winner.name}!",
                             "board": format_board_to_text(board)})

        # Save move
        Move.objects.create(
            game=game,
            player=player,
            from_row=from_row,
            from_col=from_col,
            to_row=to_row,
            to_col=to_col
        )

        # AI move(if we playing with ai)
        if 'EVIL player' in (game.opponent.name, game.current_player.name):
            game.current_player, game.opponent = game.opponent, game.current_player
            game.save()
        else:
            if game.opponent.player_type == 'ai' and not winner:
                HexapawnEngine.make_ai_move(game)

        return Response({"status": "Ход принят",
                         "board": format_board_to_text(board)})
