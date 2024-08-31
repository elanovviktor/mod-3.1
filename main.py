calls = 0
def count_calls(): # первая функция
    global calls
    calls += 1 # так называемый счетчик будщих функций.
def string_info(string) : # вторая функция, принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в
                     # верхнем регистре, строку в нижнем регистре.
    count_calls()
    return (len(string), string.upper(), string.lower()) # lowwer и upper преоразует нижний регистр в вехний и наоборот.
def is_contains( string, list_to_search):# еще одна функция, здесь два параметра
    count_calls()
    return string.upper() in[s.upper() if True else None for s in list_to_search]
# Вывод в консоль, просто скопировал из ДЗ
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)# показывает колво вызовов функций