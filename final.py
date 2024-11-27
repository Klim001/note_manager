username = input("Введите ваше имя: ")
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
title_list = [title1, title2, title3]
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