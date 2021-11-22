# Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. СПисок можна "захардкорити". Елементами списку повинні бути як рядки, так і числа.

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([2, 3, 13, 4]))
