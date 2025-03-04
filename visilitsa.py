import random

WORDS_LIST = ['do', 'car', 'life', 'block', 'garden', 'bedroom']


# Выбор слова из списка рандомно
def word_choice():
    selected_word = random.choice(WORDS_LIST)
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


# Основной цикл игры. Наверное можно было бы её разбить на несколько других функций.
# Например, условия выигрыша/проигрыша и цикл j отдельно, но я не очень представляю как.
def number_of_letter(selected_word):
    # Массив из прочерков, который обновляется по ходу угадывания букв
    word = []
    length = len(selected_word)
    for z in range(length):
        word.append('_')
    health = 10
    counter_for_win = 0

    while True:
        check_letter = input(str())
        counter_mistakes = 0
        for j in range(length):
            letter = (selected_word[j])
            if letter == check_letter:
                counter_for_win += 1
                word.pop(j)
                word.insert(j, check_letter)
                print(f'Введённая буква "{check_letter}" стоит в позиции {j + 1}')
                format_word = ' '.join(word)
                print(format_word)
            else:
                counter_mistakes += 1

        if counter_mistakes >= length:
            health -= 1
            print(f'Такой буквы нет, осталось жизней {health} ')

        if health == 0:
            print('Проигрыш')
            break

        if counter_for_win != length:
            continue
        print('Выигрыш!')
        break


selected_word = word_choice()
letters = make_letters(selected_word)

print('Шаблон для угадывания:', make_dashes())
number_of_letter(selected_word)
