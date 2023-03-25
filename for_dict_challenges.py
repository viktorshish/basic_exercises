print('Задание №1')
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

def count_repeat_names(children):
    name_counts = {}
    for student in children:
        comparison_name = student['first_name']
        if comparison_name in name_counts:
            name_counts[comparison_name] += 1
        else:
            name_counts[comparison_name] = 1
    return name_counts

count_names = count_repeat_names(students)
for name, count in count_names.items():
    print(f'{name}: {count}')

print()

print('Задание №2')
# # Дан список учеников, нужно вывести самое часто повторящееся имя
# # Пример вывода:
# # Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

count_names = count_repeat_names(students)
counts_max_name = max(count_names, key=count_names.get)
print(f'Самое частое имя среди учеников: {counts_max_name}')

print()

print('Задание №3')
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:``
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for number_group, group in enumerate(school_students, 1):
    name_counts = {}
    for student in group:
        name_student = student['first_name']
        if name_student in name_counts:
            name_counts[name_student] += 1
        else:
            name_counts[name_student] = 1
    max_count_name = max(name_counts, key=name_counts.get)
    print(f'Самое частое имя в классе {number_group}: {max_count_name}')

print()

print('Задание №4')
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

# 1) разбить на классы - пройтись циклом по классам
for group in school:
    # 2) Пройтись циклом по студентам
    count_girl = 0
    count_boy = 0
    for student in group['students']:
        name_student = student['first_name']
        # 3) Разобраться кто в классе мальчик, а кто девочка
        if is_male[name_student]:
            count_boy += 1
        else:
            count_girl += 1
    print(f'Класс {group["class"]}: девочки {count_girl}, мальчики {count_boy}')

print()

print('Задание №5')
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]   },
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
male_counts = {}
female_counts = {}

for group in school:
    class_name = group['class']
    male_counts[class_name] = 0
    female_counts[class_name] = 0
    for student in group['students']:
        name = student['first_name']
        if is_male[name]:
            male_counts[class_name] += 1
        else:
            female_counts[class_name] += 1

max_male_class = max(male_counts, key=male_counts.get)
max_female_class = max(female_counts, key=female_counts.get)

print(f'Больше всего мальчиков в классе {max_male_class}')
print(f'Больше всего девочек в классе {max_female_class}')

