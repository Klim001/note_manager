username = input("Введите ваше имя: ")
title_list = []
#ввод заголовков
while(1):
    title = input("Введите заголовок (или оставьте пустым для завершения): ")
    if title == "":
        break  #завершение при пустом вводе
    if title in title_list:
        print("заголовок уже существует")
    else:
        title_list.append(title)  #добавление после проверки на уникальность и пустоту


content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ожидает, готово, в работе.: ")
created_date = input("Введите дату создания заметки в формате xx-xx-xxxx: ")
issue_date = input("Введите дату истечения заметки в формате xx-xx-xxxx: ")
data_dict = {"Имя пользователя" : username,
             "Заголовки заметки": title_list,
             "Описание заметки" : content,
             "Статус заметки" : status,
             "Дата создания заметки" : created_date,
             "Дата истечения заметки" : issue_date,
             }
print(data_dict)
temp_created_date = created_date[:5]
temp_issue_date = issue_date[:5]
print(temp_created_date)
print(temp_issue_date)