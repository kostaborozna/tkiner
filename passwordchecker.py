
def password_check(password):
    if len(password) < 8:
        return 'Богу не понравился ваш пароль. Надо подлинее 😳😳😳'
    elif count_uppercase_letters(password) < 2:
        return 'Богу не понравился ваш пароль. Добавь большие буковки 🥵🥵🥵'
    elif count_digits(password) < 2:
        return 'Богу не понравился ваш пароль. Добавь цифарки 🤓🤓🤓'
    else:
        return 'Какой ты молодец. Добро пожаловать в рай ✅✅✅💖💗🥰💞'

def count_uppercase_letters(word):
    count = 0
    for letter in word:
        if letter.isupper():
            count += 1
    return count

def count_digits(word):
    count = 0
    for letter in word:
        if letter.isdigit():
            count += 1
    return count



