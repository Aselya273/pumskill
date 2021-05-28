cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]
    
city = input('Введите город: ')

if city.lower()==tourists[0]['city'].lower(): 
    print(f"Турист {tourists[0]['user']['name']} возраст {tourists[0]['user']['age']} лет, посетил город {city}")
elif city.lower()==tourists[1]['city'].lower():
    print(f"Турист {tourists[1]['user']['name']} возраст {tourists[1]['user']['age']} года, посетила город {'city'}")
elif city.lower()==tourists[2]['city'].lower():
    print(f"Турист {tourists[2]['user']['name']} возраст {tourists[2]['user']['age']} лет, посетила город {'city'}")
else:
    print('Такого города нет')

    
    # fibonace=[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,
    #      4181,6765,10946,17711,28657,46368,75025,121393,196418,
    #      317811,514229,832040,1346269,2178309,3524578,5702887,
    #      9227465]
