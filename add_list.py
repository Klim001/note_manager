username = input("Введите ваше имя: ")
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
title_list = [title1, title2, title3]
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ожидает, готово, в работе.: ")
created_date = input("Введите дату создания заметки в формате xx-xx-xxxx: ")
issue_date = input("Введите дату истечения заметки в формате xx-xx-xxxx: ")

print("Имя пользователя: ", username)
print("Заголовки заметки: ", *title_list)
print("Описание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", created_date)
print("Дата истечения заметки: ", issue_date)
temp_created_date = created_date[:5]
temp_issue_date = issue_date[:5]
print(temp_created_date)
print(temp_issue_date)