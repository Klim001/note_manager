'''
1. Напишите функцию search_notes(notes, keyword=None, status=None), которая:
Принимает список заметок (notes), ключевое слово (keyword) и/или статус (status) в качестве аргументов.
Возвращает список заметок, которые соответствуют заданным критериям поиска.

2. Реализуйте следующий функционал:
Поиск по ключевым словам:
Заметки отбираются, если заданное ключевое слово встречается в любом из полей: title, content, или username.
Поиск по статусу:
Заметки отбираются, если их поле status совпадает с указанным.
Если указаны оба параметра (keyword и status), выполняйте поиск с учётом обоих условий.
Программа должна выводить найденные заметки в удобном формате. Если заметки не найдены, выведите сообщение:
Заметки, соответствующие запросу, не найдены.

3. Обеспечьте обработку пустого списка заметок.
'''

from datetime import *
from fnmatch import *


def date_today():  # текущая дата
    today = str(datetime.today())[:10]
    today = today.split("-")
    today.reverse()
    today_date = "-".join(today)
    return today_date


def differ_date(today, issue):  # количество дней до дедлайна
    today = today.split("-")
    issue = issue.split("-")
    today = [int(x) for x in today]
    issue = [int(x) for x in issue]
    if today[2] == issue[2] and today[1] == issue[1] and today[0] == issue[0]:
        return 0
    diff = date(today[2], today[1], today[0]) - date(issue[2], issue[1], issue[0])
    diff = str(diff)
    diff = diff[:-13]
    diff = int(diff)
    if diff < 0:
        print(f"До дедлайна осталось {abs(diff)} дня.")
    if diff == 0:
        print("Дедлайн сегодня!")
    if diff > 0:
        print(f"Внимание! Дедлайн истёк {abs(diff)} дня назад.")


def input_date():  # ввод даты истечения срока
    date1 = ""
    while not fnmatch(str(date1), "??-??-????"):
        try:
            date = input("Введите дату дедлайна в формате день-месяц-год (xx-xx-xxxx): ")
            date = date.split('-')
            date = [int(x) for x in date]
            date1 = []
            for i in date:
                if i < 10:
                    date1.append("0" + str(i))
                else:
                    date1.append(str(i))
            date1 = str(date1[0]) + "-" + str(date1[1]) + "-" + str(date1[2])
        except ValueError:
            print("Соблюдайте формат ввода")
    return str(date1)


def new_note():  # создание новой заметки
    issue_date = input_date()
    differ_date(created_date, issue_date)
    username = input("Введите ваше имя: ")
    title_list = []

    while True:  # ввод заголовков
        title = input("Введите заголовок (или оставьте пустым для завершения): ")
        if title == "":
            break  # завершение при пустом вводе
        if title in title_list:
            print("заголовок уже существует")
        else:
            title_list.append(title)  # добавление после проверки на уникальность и пустоту

    content = input("Введите описание заметки: ")
    status = ["выполнено", "в процессе", "отложено"]
    data_dict = {"Имя пользователя": username,
                 "Заголовки заметки": title_list,
                 "Описание заметки": content,
                 "Статус заметки": status[1],
                 "Дата создания заметки": created_date,
                 "Дата истечения заметки": issue_date
                 }
    print("Выберите новый статус заметки:\n1. выполнено\n2. в процессе\n3. отложено")
    ind = int(input("Введите порядковый номер: "))
    print(f"Статус заметки успешно обновлён на: {status[ind - 1]}")
    data_dict["Статус заметки"] = status[ind - 1]
    notes.append(data_dict)

def create_note():  #создание заметки
    new_note()
    print("Заметка создана:")
    print("-" * 150)
    for j in notes[-1]:
        print(j, ":", notes[-1][j])
    print("-" * 150)

def output():  # вывод заметок
    print("-" * 150)
    for i in range(len(notes)):
        for j in notes[i]:
            print(j, ":", notes[i][j])
        print("-" * 150)

def delete_note(title):  # удаление заметки
    for i in range(len(notes)):
        title_list_lower = [str(x).lower() for x in notes[i]["Заголовки заметки"]]
        if title.lower() in title_list_lower:
            notes.remove(notes[i])
            break
    else:
        print("Такой заметки не найдено")

def update_note(note):  #обновление заметки
    print("-" * 150)
    for j in note:
        print(j, ":", note[j])
    print("-" * 150)
    print("Какие данные вы хотите обновить?\n"
          "1. Имя пользователя\n"
          "2. Заголовки заметки\n"
          "3. Описание заметки\n"
          "4. Статус заметки\n"
          "5. Дата создания заметки\n"
          "6. Дата истечения заметки\n")
    num = 0
    while num not in [1, 2, 3, 4, 5]:
        try:
            num = int(input("Выберите порядковый номер: "))
        except ValueError:
            print("Соблюдайте формат ввода")
    if num == 5:
        name = list(note.keys())[num]
    else:
        name = list(note.keys())[num - 1]
    if num == 5:
        new_st = input_date()
    else:
        new_st = input(f"Введите новое значение для {name}: ")
    note[name] = new_st
    print("Заметка обновлена: ")
    print("*" * 150)
    for j in note:
        print(j, ":", note[j])
    print("*" * 150)

def display_notes(notes):  #вывод заметок
    if len(notes) == 0:
        print("У вас нет сохранённых заметок.")
        return
    print("Список заметок: ")
    print("-" * 150)
    for i in range(len(notes)):
        print(f"Заметка №{i + 1}")
        for j in notes[i]:
            print(j, ":", notes[i][j])
        print("-" * 150)

def search_notes(notes, keyword):  #поиск заметок
    notes_match = []
    for i in range(len(notes)):
        for j in notes[i]["Заголовки заметки"]:
            if keyword.lower() in j.lower():
                notes_match.append(notes[i])
        if keyword.lower() in notes[i]["Имя пользователя"].lower() or\
            keyword.lower() in notes[i]["Описание заметки"].lower():
            notes_match.append(notes[i])
    if len(notes_match) > 0:
        return notes_match
    else:
        print("Заметки, соответствующие запросу, не найдены.")
        return []

if __name__ == "__main__":
    notes = []
    print("Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.")
    created_date = date_today()
    print("Текущая дата: ", created_date)

    new_note()
    display_notes(notes)
    while True:
        new = input("Хотите добавить ещё одну заметку? (да/нет): ")
        if new.lower() != "да":
            break
        create_note()

    display_notes(notes)
    delete_title = input("Введите заголовок заметки для её удаления: ")
    delete_note(delete_title)
    display_notes(notes)
    update = input("Введите заголовок заметки для обновления: ")
    ind_dict = 0
    flag = 0
    for i in range(len(notes)):
        title_list_lower = [str(x).lower() for x in notes[i]["Заголовки заметки"]]
        if update.lower() in title_list_lower:
            ind_dict = i
            flag = 1
            break
    if flag == 1:
        update_note(notes[ind_dict])
    keyword = input("Введите ключевое слово для поиска заметки: ")
    match = search_notes(notes, keyword)
    display_notes(match)