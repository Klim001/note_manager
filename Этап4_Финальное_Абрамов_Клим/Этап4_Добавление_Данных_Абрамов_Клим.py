'''
Описание задачи:
Создать функцию append_notes_to_file(notes, filename), которая:
    Добавляет новые заметки в существующий файл, сохраняя старые данные.
    Формат записи аналогичен save_notes_to_file, но файл открывается в режиме добавления.
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
    display_notes(notes)


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
    flag_search = 0
    for i in range(len(notes)):
        for j in notes[i]["Заголовки заметки"]:
            if keyword.lower() in j.lower():
                notes_match.append(notes[i])
                flag_search = 1
        if flag_search == 1:
            continue
        if keyword.lower() in notes[i]["Имя пользователя"].lower() or\
            keyword.lower() in notes[i]["Описание заметки"].lower():
            notes_match.append(notes[i])
    if len(notes_match) > 0:
        return notes_match
    else:
        print("Заметки, соответствующие запросу, не найдены.")
        return

def menu():  #Меню действий
    global mark
    save_notes_to_file(notes, "text.txt")
    print("Меню действий:\n"
          "1. Создать новую заметку\n"
          "2. Показать все заметки\n"
          "3. Обновить заметку\n"
          "4. Удалить заметку\n"
          "5. Найти заметки\n"
          "6. Выйти из программы\n")
    num = 0
    while num not in [1, 2, 3, 4, 5, 6]:
        try:
            num = int(input("Введите номер: "))
        except ValueError:
            print("Соблюдайте формат ввода")
        if num not in [1, 2, 3, 4, 5, 6]:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")
    if num == 1:
        create_note()
        #notes_append = []
        append_notes_to_file(notes, "tt.txt")
        return
    if num == 2:
        display_notes(notes)
        return
    if num == 3:
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

        return
    if num == 4:
        delete_title = input("Введите заголовок заметки для её удаления: ")
        delete_note(delete_title)
        return
    if num == 5:
        keyword = input("Введите ключевое слово для поиска заметки: ")
        match = search_notes(notes, keyword)
        display_notes(match)
        return
    if num == 6:
        mark = 0
        return

def save_notes_to_file(notes, filename):  #Сохранение заметок в файле
    with open(filename, "w", encoding='utf-8') as file:
        file.write("-" * 160 + "\n")
        for i in range(len(notes)):
            for j in notes[i]:
                file.write(str(j) + " : " + str(notes[i][j]) + "\n")
            file.write("-" * 160 + "\n")

def load_notes_from_file(filename):  #Чтение заметок из текстового файла
    data_list = []
    try:
        with open(filename, "r", encoding='utf-8') as file:
            st = file.readlines()
            dict_ = {}
            for i in range(1, len(st)):
                if i % 7 == 0:
                    data_list.append(dict_)
                    continue
                string = st[i].split(" : ")
                if i % 7 == 2:
                    list_st = string[1][1:-2:].split(", ")
                    list_st = [str(x)[1:-1] for x in list_st]
                    dict_[string[0]] = list_st
                    continue
                dict_[string[0]] = string[1][:-1:]
    except FileNotFoundError:
        with open(filename, "w"):
            pass
        print(f"Файл {filename} не найден. Создан новый файл.")
    except UnicodeDecodeError:
        print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое.")
    except Exception as e:
        print(f"Ошибка: {e}")
    return data_list

def append_notes_to_file(notes, filename):  #Добавление заметок в текстовый файл
    try:
        file = open(filename, "a", encoding='utf-8')
    except Exception as e:
        print(f"Ошибка: {e}")
    file.write("-" * 160 + "\n")
    for j in notes[-1]:
        file.write(str(j) + " : " + str(notes[-1][j]) + "\n")
    file.write("-" * 160 + "\n")


if __name__ == "__main__":
    notes = []
    print("Добро пожаловать в менеджер заметок!")
    created_date = date_today()
    print("Текущая дата: ", created_date)
    last_index = 0
    mark = 1
    while mark == 1:
        menu()
    print("Программа завершена. Спасибо за использование!")

    notes = load_notes_from_file("text.txt")
    print(notes)


