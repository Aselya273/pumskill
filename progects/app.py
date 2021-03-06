string = """name:Иван
name:Петр
name:Марья
name:Дарья
name:Юля"""

# Разделяем строку на элементы, используя разделитель - перенос строки
elements = string.split('\n')

# Создадим список, в котором будем хранить имена пользователей
user_list = []

for string in elements:
    # Разделяем каждый элемент списка elements по разделителю ':'
    # В результате у нас получится 2 элемента: 1ый - 'name', 2ой - имя пользователя
    words = string.split(':')

    # Добавляем в список пользователей второй элемент из полученного списка words
    # Помним что индексы элементов в Python начинаются с 0, поэтому у второго элемента индекс = 1
    user_list.append(words[1])

# Выводим результат
print(user_list)
