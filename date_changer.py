username = "Name"
title = "heading"
content = "description"
status = "ожидает, готово, в работе"
created_date = "19-03-2024"
issue_date = "25-11-2024"
print("Имя пользователя: ", username)
print("Заглавие заметки: ", title)
print("Описание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", created_date)
print("Дата истечения заметки: ", issue_date)
temp_created_date = created_date[:5]
temp_issue_date = issue_date[:5]
print(temp_created_date)
print(temp_issue_date)