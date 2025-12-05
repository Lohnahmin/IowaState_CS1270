# Name Lyle Osburne 11/10/2025
# Lab week 10
# Pytest unit tests for fourInSequence.py

import pytest
from fourInSequence import checkForNextMoveWin, checkAdjacent, checkDraw, checkWinner

def make_empty_board():
    return [["." for _ in range(7)] for _ in range(6)]

def make_full_board():
    return [["X" for _ in range(7)] for _ in range(6)]

def test_checkWinner_no_winner_on_empty_board():
    board = make_empty_board()
    assert checkWinner(board, 1) is False
    assert checkWinner(board, 2) is False

def test_checkWinner_horizontal_win_player1():
    board = make_empty_board()
    board[5][0] = "X"
    board[5][1] = "X"
    board[5][2] = "X"
    board[5][3] = "X"
    assert checkWinner(board, 1) is True
    assert checkWinner(board, 2) is False

def test_checkWinner_vertical_win_player2():
    board = make_empty_board()
    board[2][3] = "O"
    board[3][3] = "O"
    board[4][3] = "O"
    board[5][3] = "O"
    assert checkWinner(board, 2) is True
    assert checkWinner(board, 1) is False

def test_checkWinner_negative_diagonal_win_player1():
    board = make_empty_board()
    board[0][0] = "X"
    board[1][1] = "X"
    board[2][2] = "X"
    board[3][3] = "X"
    assert checkWinner(board, 1) is True
    assert checkWinner(board, 2) is False

def test_checkWinner_positive_diagonal_win_player2():
    board = make_empty_board()
    board[3][0] = "O"
    board[2][1] = "O"
    board[1][2] = "O"
    board[0][3] = "O"
    assert checkWinner(board, 2) is True
    assert checkWinner(board, 1) is False

def test_checkDraw_false_when_board_not_full():
    board = make_empty_board()
    board[5][0] = "X"
    assert checkDraw(board) is False

def test_checkDraw_true_when_board_full():
    board = make_full_board()
    assert checkDraw(board) is True

def test_checkAdjacent_returns_minus_one_when_no_adjacent():
    board = make_empty_board()
    assert checkAdjacent(board, 1) == -1

def test_checkAdjacent_returns_adjacent_column_for_player1():
    board = make_empty_board()
    board[5][3] = "X"
    col = checkAdjacent(board, 1)
    assert col in {2, 3, 4, -1} is False or col in {2, 3, 4}

def test_checkForNextMoveWin_finds_horizontal_winning_move():
    board = make_empty_board()
    board[5][0] = "X"
    board[5][1] = "X"
    board[5][2] = "X"
    col = checkForNextMoveWin(board, 1)
    assert col == 3

def test_checkForNextMoveWin_returns_minus_one_when_no_winning_move():
    board = make_empty_board()
    board[5][0] = "X"
    board[5][2] = "X"
    col = checkForNextMoveWin(board, 1)
    assert col == -1
