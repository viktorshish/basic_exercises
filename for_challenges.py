# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

print('Задание №1')

names = ['Оля', 'Петя', 'Вася', 'Маша']

def ex1():
    for name in names:
        print(name)

ex1()

print()

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

print('Задание №2')

names = ['Оля', 'Петя', 'Вася', 'Маша']

def ex2():
    for name in names:
        print(f'{name}: {len(name)}')

ex2()

print()

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

print('Задание №3')

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

def ex3():
    for name in names:
        if is_male[name]:
            gender = 'мужской'
        else:
            gender = 'женский'
        print(f'{name} - {gender}')

ex3()

print()

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

print('Задание №4')

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]

def ex4():
    print(f'Всего {len(groups)} группы')
    for num, group  in enumerate(groups, 1):
        print(f'Группа {num}: {len(group)}')

ex4()

print()

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

print('Задание №5')


groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

def ex5():
    for num, group in enumerate(groups, 1):
        string_name = ", ".join(group)
        print(f'Группа {num}: {string_name}')

ex5()
