
def plutal_form(quantity, word_1, word_2, word_3):
    
    """ 
    :param quantity: = цифры
    :param word_1: = яблоко/студент
    :param word_2: = яблока/студента
    :param word_3: = яблок/студентов
    
    """
    new_lists = []
    quantity = str(quantity)
    for i in quantity:
        i = int(i)
        new_lists.append(i)
        
    if new_lists[-1] == 1:
        if new_lists[-2:] == [1,1]:
            print(f'{quantity} {word_3}')
        else:
            print(f'{quantity} {word_1}')
    elif new_lists[-1] in range(2, 5):
        if new_lists[-2:] == [1, 2] or new_lists[-2:] == [1, 3] or new_lists[-2:] == [1, 4]:
            print(f'{quantity} {word_3}')
        else:
            print(f'{quantity} {word_2}')
    else:
       print(f'{quantity} {word_3}')


plutal_form(1, "яблоко", "яблока", "яблок")
plutal_form(5, "студент", "студента", "студентов") 
plutal_form(2, "яблоко", "яблока", "яблок")
