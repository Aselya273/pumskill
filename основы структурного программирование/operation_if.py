# создаем список городов.
cities=['Москва', 'Париж','Лондон']

# создаем  список состоящий из словарей. 
users=[{'name': 'Иван', 'age': '35'},
       {'name': 'Мария', 'age': '26'},
       {'name': 'Максим', 'age':'31'}]

# создаем список состоящий из словарей,которому обращаемся по индексу.
tourist =[{'user': users[0], 'city': cities[2]}, # Имя Иван, город Лондон
         {'user': users[1], 'city': cities[0]},  # Имя Мария, город Москва
         {'user': users[2], 'city': cities[1]}]  # Имя Максим, город Париж

# создаем пользовательский ввод.
city=input('Введите город: ')
 
   
    
# Проверяем используя конструкцию if,elif,else.
# С помощью lower()передаем в нижний регистр.
if city.lower() == tourist[0]['city'].lower():
    print(f"Турист {tourist[0]['user']['name']}, возраст {tourist[0]['user']['age']} лет, посетил {city}")
elif city.lower() == tourist[1]['city'].lower():
    print(f"Турист {tourist[1]['user']['name']}, возраст {tourist[1]['user']['age']} лет, посетила {city}")   
elif city.lower() == tourist[2]['city'].lower():
    print(f"Турист {tourist[2] ['user']['name']}, возраст {tourist[2]['user']['age']} год,посетил {city}")
    
# В случае если ввести город которого нет,то нужно вывести это сообщение.
else:
    print("Такого города нет в базе данных")
    
