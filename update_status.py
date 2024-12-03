username = input("Введите ваше имя: ")
title_list = []
#ввод заголовков
while (1):
    title = input("Введите заголовок (или оставьте пустым для завершения): ")
    if title == "":
        break  #завершение при пустом вводе
    if title in title_list:
        print("заголовок уже существует")
    else:
        title_list.append(title)  #добавление после проверки на уникальность и пустоту

content = input("Введите описание заметки: ")
status = ["выполнено", "в процессе", "отложено"]
created_date = input("Введите дату создания заметки в формате xx-xx-xxxx: ")
issue_date = input("Введите дату истечения заметки в формате xx-xx-xxxx: ")

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
