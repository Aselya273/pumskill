#определяем начальные значения начального и конечного числа
#ОБРАТИТЕ ВНИМАНИЕ, что в начале цикла второе число меньше первого на единицу
number_up_to,number_after = 1, 0
#начальное значение суммы
summ_up_after = 0
#число финиша цикла
number_finish = int(input("Введите число завершения цикла: "))
print('______________________________________________________')
print(f'Числа Фибоначчи до {number_finish}.')
#список чисел последовательности
list_sequence = []
#основной цикл прерывать его будем по сумме двух чисел
while number_up_to + number_after < number_finish:
	#получаем сумму двух чисел
	summ_up_after = number_up_to + number_after
	#заполняем список полученными числами
	if summ_up_after < number_finish:
		list_sequence.append(summ_up_after)
	#первое меняем на второе
	number_up_to = number_after
	#второе приравниваем к сумме
	number_after = summ_up_after
	#выводим сумму
	print(summ_up_after)
    
print('______________________________________________________')
	
#количество элементов в последовательности
print(f'Количество элементов в последовательности: {len(list_sequence)}')
print('______________________________________________________')
#список четных членов последовательности
print("Четные члены последовательности: ")        
#list comprehension
even_members_sequence = [print(num) for num in list_sequence if num % 2 == 0]
print('______________________________________________________')		
#сумма всех четных членов последовательности
print(f'Сумма всех четных членов последовательности: \
{sum([num for num in list_sequence if num % 2 == 0])}')

print('______________________________________________________')
print(f'Ближайшее к 10000000 число Фибоначчи: {list_sequence[len(list_sequence) - 1]}')
print(f'Ближайшее к {number_finish} число Фибоначчи: {list_sequence[len(list_sequence) - 1]}')
