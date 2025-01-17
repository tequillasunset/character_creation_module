from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Функция атаки."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(-3, -1)}')
    return (f'{char_name} не применил специальное умение')


def defence(char_name: str, char_class: str) -> str:
    """Функция защиты."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} не применил специальное умение')


def special(char_name: str, char_class: str) -> str:
    """Функция особого умения."""
    if char_class == 'warrior':
        return (f'{char_name} применил особое умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил особое умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил особое умение «Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Функция тренировок."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — великий мастер ближнего боя.'
              'Сильный, выносливый и отважный')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.'
              'Обладает высоким интеллектом.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Команды: attack — атака, defence — блок или special — суперсила.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Функция выбора персонажа."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Войн — warrior, Маг — mage, Лекарь — healer:')
        if char_class == 'warrior':
            print('Воитель — Воитель — дерзкий воин ближнего боя.'
                  'Сильный, выносливый и отважный')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.'
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class
