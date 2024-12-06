from datetime import *
from fnmatch import *

def date_today():  #текущая дата
    today = str(datetime.today())[:10]
    today = today.split("-")
    today.reverse()
    today_date = "-".join(today)
    return today_date

def differ_date(today, issue):  #количество дней до дедлайна
    today = today.split("-")
    issue = issue.split("-")
    today = [int(x) for x in today]
    issue = [int(x) for x in issue]
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

def input_date():  #ввод даты истечения срока
    date = ""
    while not fnmatch(str(date), "??-??-????"):
        try:
            date = input("Введите дату дедлайна в формате день-месяц-год (xx-xx-xxxx): ")
            date = date.split('-')
            date = [int(x) for x in date]
            date = str(date[0]) + "-" + str(date[1]) + "-" + str(date[2])
        except ValueError:
            print("Соблюдайте формат ввода")
    return str(date)

created_date = date_today()
print("Текущая дата: ", created_date)
issue_date = input_date()
differ_date(created_date, issue_date)
username = input("Введите ваше имя: ")
title_list = []

while True:  #ввод заголовков
    title = input("Введите заголовок (или оставьте пустым для завершения): ")
    if title == "":
        break  #завершение при пустом вводе
    if title in title_list:
        print("заголовок уже существует")
    else:
        title_list.append(title)  #добавление после проверки на уникальность и пустоту

content = input("Введите описание заметки: ")
status = ["выполнено", "в процессе", "отложено"]
data_dict = {"Имя пользователя": username,
             "Заголовки заметки": title_list,
             "Описание заметки": content,
             "Статус заметки": status[1],
             "Дата создания заметки": created_date,
             "Дата истечения заметки": issue_date,
             }
print(data_dict)
temp_created_date = created_date[:5]
temp_issue_date = issue_date[:5]
print(temp_created_date)
print(temp_issue_date)
print("Выберите новый статус заметки:\n1. выполнено\n2. в процессе\n3. отложено")
ind = int(input("Введите порядковый номер: "))
print(f"Статус заметки успешно обновлён на: {status[ind - 1]}")
data_dict["Статус заметки"] = status[ind - 1]
print(data_dict)
