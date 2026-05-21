"""
Tic-Tac-Toe AI — Minimax with Alpha-Beta Pruning
=================================================
An unbeatable AI agent using game tree search.
Author: Portfolio Project 01
"""

import math
from typing import Optional

EMPTY = " "
HUMAN = "X"
AI = "O"


def create_board() -> list[list[str]]:
    return [[EMPTY] * 3 for _ in range(3)]


def print_board(board: list[list[str]]) -> None:
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(f"{i} " + " | ".join(row))
        if i < 2:
            print("  " + "-" * 9)
    print()


def get_available_moves(board: list[list[str]]) -> list[tuple[int, int]]:
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]


def check_winner(board: list[list[str]]) -> Optional[str]:
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in lines:
        if line[0] != EMPTY and line[0] == line[1] == line[2]:
            return line[0]
    return None


def is_terminal(board: list[list[str]]) -> bool:
    return check_winner(board) is not None or not get_available_moves(board)


def evaluate(board: list[list[str]]) -> int:
    winner = check_winner(board)
    if winner == AI:
        return 10
    if winner == HUMAN:
        return -10
    return 0


def minimax(
    board: list[list[str]],
    depth: int,
    is_maximizing: bool,
    alpha: float = -math.inf,
    beta: float = math.inf,
) -> int:
    """
    Minimax with Alpha-Beta pruning.
    alpha: best score the maximizer can guarantee
    beta:  best score the minimizer can guarantee
    """
    if is_terminal(board):
        score = evaluate(board)
        return score - depth if score > 0 else score + depth  # prefer faster wins

    if is_maximizing:
        best = -math.inf
        for r, c in get_available_moves(board):
            board[r][c] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[r][c] = EMPTY
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:  # beta cut-off
                break
        return best
    else:
        best = math.inf
        for r, c in get_available_moves(board):
            board[r][c] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[r][c] = EMPTY
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:  # alpha cut-off
                break
        return best


def best_move(board: list[list[str]]) -> tuple[int, int]:
    """Return the AI's best move."""
    best_score = -math.inf
    move = (-1, -1)
    for r, c in get_available_moves(board):
        board[r][c] = AI
        score = minimax(board, 0, False)
        board[r][c] = EMPTY
        if score > best_score:
            best_score = score
            move = (r, c)
    return move


def play_game() -> None:
    board = create_board()
    print("=" * 40)
    print("   TIC-TAC-TOE AI  (Minimax + α-β)")
    print("   You = X   |   AI = O")
    print("=" * 40)
    print_board(board)

    current_player = HUMAN  # Human goes first

    while not is_terminal(board):
        if current_player == HUMAN:
            while True:
                try:
                    row = int(input("Your move — row (0-2): "))
                    col = int(input("Your move — col (0-2): "))
                    if (row, col) in get_available_moves(board):
                        board[row][col] = HUMAN
                        break
                    print("Cell taken, try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter 0, 1, or 2.")
        else:
            print("AI is thinking...")
            r, c = best_move(board)
            board[r][c] = AI
            print(f"AI played: row={r}, col={c}")

        print_board(board)
        current_player = AI if current_player == HUMAN else HUMAN

    winner = check_winner(board)
    if winner:
        print(f"🏆 {winner} wins!" if winner == HUMAN else "🤖 AI wins! (Minimax is unbeatable)")
    else:
        print("🤝 It's a draw!")


if __name__ == "__main__":
    play_game()
