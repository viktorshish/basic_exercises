"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов с суммарным налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов с указанием месячной налоговой нагрузки – количеством денег, которые в месяц этот отдел платит налогами.
16. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# 1. Вывести названия всех отделов
print('Задание 1')

for department in departments:
    print(department['title'])
print()

# 2. Вывести имена всех сотрудников компании.
print('Задание 2')

for department in departments:
    for employee in department['employers']:
        print(employee['first_name'])
print()

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
print('Задание 3')

for department in departments:
    for employee in department['employers']:
        print(f"{employee['first_name']} работает в отделе: {department['title']}")
print()

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
print('Задание 4')

for department in departments:
    comparative_salary = 100000
    for employee in department['employers']:
        if employee['salary_rub'] > comparative_salary:
            print(f'{employee["first_name"]} получает больше {comparative_salary} рублей')
print()

# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
print('Задание 5')

for department in departments:
    comparative_salary = 80000
    for employee in department['employers']:
        if employee['salary_rub'] < comparative_salary:
            print(f'На позиции {employee["position"]} получают меньше {comparative_salary} рублей')
print()

# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
print('Задание 6')
for department in departments:
    money_spent_department = 0
    for employee in department['employers']:
        money_spent_department += employee['salary_rub']
    print(f'Отдел: {department["title"]} потратил {money_spent_department} рублей')
