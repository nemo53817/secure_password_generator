import random


def ask_question_and_get_yes_no_answer(question):
    yes_no_str = " yes/no/y/n"
    answer = input(question + yes_no_str + '\n').lower().strip()
    while answer != 'yes' and answer != 'y' and answer != 'no' and answer != 'n':
        print("Please type yes/no/y/n as answer")
        answer = input(question + yes_no_str + '\n').lower().strip()

    if answer == 'yes' or answer == 'y':
        return True
    else:
        return False


def generate_and_print_passwords(passwords_number, password_len, symbols_set_indexes, use_ambiguous_symbols):
    symbols_range_list = [
        '0123456789',
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '!#$%&*+-=?@^_'
    ]

    ambiguous_symbols = 'il1Lo0O'

    [
        print('password number', i,
              generate_password(password_len, symbols_range_list, symbols_set_indexes, ambiguous_symbols,
                                use_ambiguous_symbols))
        for i in range(1, passwords_number + 1)
        ]


def generate_password(password_len, symbols_set, symbols_set_indexes, ambiguous_symbols_set, use_ambiguous_symbols):
    password = ''
    number_of_chars_generated = 0

    while number_of_chars_generated < len(symbols_set_indexes):
        password += generate_random_char_from_set(symbols_set[symbols_set_indexes[number_of_chars_generated]],
                                                  ambiguous_symbols_set,
                                                  use_ambiguous_symbols)
        number_of_chars_generated += 1

    while number_of_chars_generated < password_len:
        symbols_set_index = random.randrange(len(symbols_set_indexes))
        password += generate_random_char_from_set(symbols_set[symbols_set_indexes[symbols_set_index]],
                                                  ambiguous_symbols_set,
                                                  use_ambiguous_symbols)
        number_of_chars_generated += 1

    return ''.join(random.sample(password, len(password)))


def generate_random_char_from_set(symbol_set, ambiguous_char_set, use_ambiguous_symbols):
    if use_ambiguous_symbols:
        return symbol_set[random.randrange(len(symbol_set))]
    else:
        while True:
            c = symbol_set[random.randrange(len(symbol_set))]
            if c not in ambiguous_char_set:
                return c
            else:
                continue


symbols_to_use_indexes = list()

min_password_length = 1
max_password_length = 50
password_length = int(input(
    f"Specify password length. Minimum:{min_password_length}, maximum, {max_password_length}\n"))

if password_length < min_password_length or password_length > max_password_length:
    print('Password length must be greater or equal than', min_password_length, 'and less or equal than',
          max_password_length)
    exit(1)

min_passwords_number = 1
max_passwords_number = 100
passwords_count = int(input("Specify passwords number:\n"))
if passwords_count < min_passwords_number or passwords_count > max_passwords_number:
    print('Passwords number must be greater or equal than', min_passwords_number, 'and less or equal than',
          max_passwords_number)
    exit(1)

use_digits = ask_question_and_get_yes_no_answer("Use digits?")
if use_digits:
    symbols_to_use_indexes.append(0)

use_lower_letters = ask_question_and_get_yes_no_answer("Use lowercase letters?")
if use_lower_letters:
    symbols_to_use_indexes.append(1)

use_upper_letters = ask_question_and_get_yes_no_answer("Use uppercase letters?")
if use_upper_letters:
    symbols_to_use_indexes.append(2)

use_special_symbols = ask_question_and_get_yes_no_answer("Use special symbols?")
if use_special_symbols:
    symbols_to_use_indexes.append(3)

if len(symbols_to_use_indexes) == 0:
    print('You must specify at least one category of symbols!')
    exit(1)

if len(symbols_to_use_indexes) > password_length:
    print('Password length must be greater or equal than number of categories of symbols selected')
    exit(1)

use_amb_symbols = ask_question_and_get_yes_no_answer("Use ambiguous symbols?")

random.shuffle(symbols_to_use_indexes)

generate_and_print_passwords(passwords_count, password_length, symbols_to_use_indexes, use_amb_symbols)
