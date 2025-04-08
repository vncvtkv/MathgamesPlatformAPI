import random
from django.core.exceptions import ValidationError
from .models import Move


class HexapawnEngine:

    @staticmethod
    def validate_move(board, from_row, from_col, to_row, to_col, player):
        """Check rules of Hexapawn"""
        piece = board[from_row][from_col]
        target = board[to_row][to_col]
        direction = 1 if player.player_type == 'human' else -1

        # Checking the shape's ownership
        expected_piece = 'W' if player.player_type == 'human' else 'B'
        if piece != expected_piece:
            raise ValidationError("This is not your figure")

        # Check the movement rules
        if from_col == to_col:  # Move forward
            if to_row != from_row + direction:
                raise ValidationError("Pawns only move forward")
            if target != '.':
                raise ValidationError("You can't go to an occupied cell")
        elif abs(from_col - to_col) == 1:  # Взятие
            if to_row != from_row + direction:
                raise ValidationError("A diagonal move of only one square")
            expected_target = 'B' if player.player_type == 'human' else 'W'
            if target != expected_target:
                raise ValidationError("You can only hit the opponent's pieces")
        else:
            raise ValidationError("An unacceptable move")

    @staticmethod
    def check_winner(board, player):
        """Checks the victory conditions"""
        num_B, num_W = 0, 0

        # The pawn has reached the end
        for col in range(3):
            if board[0][col] == 'B':
                return 'B'
            if board[2][col] == 'W':
                return 'W'

        # All the pawns are eaten
        for i in range(len(board)):
            for j in range(len(board[0])):
                num_W += board[i][j] == 'W'
                num_B += board[i][j] == 'B'
        if num_W == 0:
            return 'B'
        if num_B == 0:
            return 'W'

        possible_moves = HexapawnEngine.get_possible_moves(board, player)
        if possible_moves == []:
            return 'win'
        return None

    @staticmethod
    def get_possible_moves(board, player):
        """Returns all possible moves for the specified player"""
        possible_moves = []
        piece = 'W' if player.player_type == 'human' else 'B'
        direction = 1 if player.player_type == 'human' else -1

        for row in range(3):
            for col in range(3):
                if board[row][col] == piece:
                    # Ход вперед
                    new_row = row + direction
                    if 0 <= new_row <= 2 and board[new_row][col] == '.':
                        possible_moves.append((row, col, new_row, col))

                    # Взятие по диагонали
                    for dcol in [-1, 1]:
                        new_col = col + dcol
                        if (0 <= new_col <= 2 and
                            0 <= new_row <= 2 and
                            board[new_row][new_col] != '.' and
                                board[new_row][new_col] != piece):
                            possible_moves.append((row, col, new_row, new_col))

        return possible_moves

    @staticmethod
    def make_ai_move(game):
        """Генерирует и выполняет ход ИИ"""
        board = game.board
        player = game.opponent
        possible_moves = HexapawnEngine.get_possible_moves(game.board, player)

        # Поиск возможных ходов для ИИ (черные пешки 'p')

        if possible_moves:
            move = random.choice(possible_moves)
            # Сохраняем ход
            Move.objects.create(
                game=game,
                player=game.opponent,
                from_row=move[0],
                from_col=move[1],
                to_row=move[2],
                to_col=move[3]
            )
            # Обновляем доску
            board[move[0]][move[1]] = '.'
            board[move[2]][move[3]] = 'B'
            game.board = board
            game.save()
            winner = HexapawnEngine.check_winner(board, game.opponent)
            if winner:
                game.winner = player
                game.save()


def format_board_to_text(board):
    """
    Maps board to rows of text
    that looks better in json
    """
    return {
        "row0": " ".join(board[0]),
        "row1": " ".join(board[1]),
        "row2": " ".join(board[2]),
    }
