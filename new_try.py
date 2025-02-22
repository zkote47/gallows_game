import random
from game_process import GameProcess
WORDS_LIST = ['do', 'car', 'life', 'block', 'garden', 'bedroom']
LIVES_NUMBER = 10

# Выбор слова из списка рандомно
def word_choice(word_list):
    selected_word = random.choice(word_list)
    print(f'Выбранное слово: {selected_word}')      # подсказка для проверки
    return selected_word


# Разбивание слова на буквы
def make_letters(selected_word):
    letters = list(selected_word)
    return letters


# длина слова, можно объединить с другой функцией, например make_dashes()
def length_of_word():
    length = len(letters)
    return length


# Создание стартовых прочерков слова
def make_dashes():
    dashes = []
    for i in range(length_of_word()):
        dashes.append('_')
    format_dashes = ' '.join(dashes)
    return format_dashes

def main_loop(selected_word: str, game_process: GameProcess):
    while not game_process.terminated:
        check_letter = input(str())
        game_step(game_process, selected_word, check_letter)
        render_step(game_process)

def game_step(process: GameProcess, selected_word, check_letter):
    process_letter_entries(process, selected_word, check_letter)

    if not process.find_letter_result:
        process.errors += 1
        process.lives -= 1

    if process.lives <= 0:
        process.terminated = True
        process.win = False
        return

    if len(process.letters_to_find) > 0:
        return
    else:
        process.win = True
        process.terminated = True
        return

def process_letter_entries(process: GameProcess, selected_word: str, check_letter: str):
    process.found_letter = None
    process.find_letter_result = False
    process.found_letter_position = []
    for j in range(len(process.word)):
        letter = (selected_word[j])
        if letter == check_letter:
            if letter in process.letters_to_find:
                process.counter_for_win += 1
                process.letters_to_find.remove(letter)
                process.word.pop(j)
                process.word.insert(j, check_letter)
            process.found_letter_position.append(j+1)
            process.found_letter = letter
            process.find_letter_result = True

def render_step(process: GameProcess):
    if process.find_letter_result:
        format_word = ' '.join(process.word)
        found_letters = render_position(process.found_letter_position)
        print(f'Введённая буква "{process.found_letter}" стоит в позиции {found_letters}')
        print(format_word)
    else:
        print(f'Такой буквы нет, осталось жизней {process.lives} ')

    if not process.win and process.terminated:
        print('Проигрыш')
        return

    if process.win and process.terminated:
        print('Выигрыш!')

def render_position(positions):
    return positions[0] if len(positions) == 1 else ', '.join([str(x) for x in positions])

if __name__ == "__main__":
    selected_word = word_choice(WORDS_LIST)
    letters = make_letters(selected_word)

    game_process = GameProcess(
        lives=LIVES_NUMBER,
        selected_word=selected_word
    )

    print('Шаблон для угадывания:', make_dashes())
    main_loop(selected_word, game_process)
