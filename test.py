from new_try import game_step
from game_process import GameProcess
import pytest

def test_base():
    word_base = "word"
    user_input = "word"

    game_process = GameProcess(
        lives=5,
        selected_word=word_base
    )

    for letter in user_input:
        game_step(game_process, word_base, letter)

    assert game_process.terminated, "Should be true" # bool, string
    assert game_process.win, "Should be true"

def test_fail_tries_exceeded():
    word_base = "word"
    user_input = "ouuuuuuuuuuuword"

    game_process = GameProcess(
        lives=5,
        selected_word=word_base
    )

    for letter in user_input:
        game_step(game_process, word_base, letter)

    assert game_process.terminated, "Should be true" # bool, string
    assert not game_process.win, "Should be false"

def test_repeating():
    word_base = "gooooooooooooooooooal"
    user_input = "gggoal"

    game_process = GameProcess(
        lives=5,
        selected_word=word_base
    )

    for letter in user_input:
        game_step(game_process, word_base, letter)

    assert game_process.terminated, "Should be true" # bool, string
    assert game_process.win, "Should be true"

def test_repeating2():
    word_base = "bedroom"
    user_input = "obedrm"

    game_process = GameProcess(
        lives=5,
        selected_word=word_base
    )

    for letter in user_input:
        game_step(game_process, word_base, letter)

    assert game_process.terminated, "Should be true" # bool, string
    assert game_process.win, "Should be true"