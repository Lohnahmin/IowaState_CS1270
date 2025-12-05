# Name Lyle Osburne 11/10/2025
# Lab week 10
# Unit tests for Rock Paper Scissors game using test driven development

import pytest
from rockPaperScissors import generateComputerMove, determineWinner, playRound

def test_generateComputerMove_returns_valid_option():
    for _ in range(50):
        move = generateComputerMove()
        assert move in ["Rock", "Paper", "Scissors"]

def test_determineWinner_rock_vs_paper():
    assert determineWinner("Rock", "Paper") == "Paper"

def test_determineWinner_rock_vs_scissors():
    assert determineWinner("Rock", "Scissors") == "Rock"

def test_determineWinner_paper_vs_scissors():
    assert determineWinner("Paper", "Scissors") == "Scissors"

def test_determineWinner_same_move_returns_draw():
    assert determineWinner("Rock", "Rock") == "Draw"
    assert determineWinner("Paper", "Paper") == "Draw"
    assert determineWinner("Scissors", "Scissors") == "Draw"

def test_playRound_human_wins():
    def fakeComp(): return "Scissors"
    comp = fakeComp()
    assert determineWinner("Rock", comp) == "Rock"

def test_playRound_computer_wins():
    def fakeComp(): return "Rock"
    comp = fakeComp()
    assert determineWinner("Scissors", comp) == "Rock"
