def to_dashes_array(length: int):
    return ['_' for _ in range(length)]


class GameProcess:
    def __init__(self, lives: int, selected_word: str):
        self.word = to_dashes_array(len(selected_word))
        self.counter_for_win = 0
        self.errors = 0
        self.win = False
        self.lives = lives
        self.terminated = False
        self.found_letter = None
        self.found_letter_position = []
        self.find_letter_result = False
        self.letters_to_find = list(selected_word)


