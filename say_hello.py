# код функции say_hello
# Если при вызове функции второй аргумент не будет указан —
# функция не сломается, а установит значением для name пустую строку
def say_hello(current_hour, name=''):
    if current_hour <= 5 or current_hour >= 23:
        hello_message = 'Доброй ночи'
    elif current_hour >= 6 and current_hour <= 11:
        hello_message = 'Доброе утро'
    elif current_hour >= 12 and current_hour <= 17:
        hello_message = 'Добрый день'
    elif current_hour >= 18 and current_hour <= 22:
        hello_message = 'Добрый вечер'
    # Проверим содержание переменной name,
    # и если это пустая строка — на печать выведем только приветствие,
    # без name
    if name == '':
        print(hello_message + '!')
    # ...а если в переменной name НЕ пустая строка — 
    # выведем на печать приветствие и имя из name
    else:
        print(hello_message + ', ' + name + '!')


# Вызовем say_hello() с двумя аргументами
say_hello(10, 'Тимур')
# Будет напечатано: Доброе утро, Тимур!

# И ещё раз вызовем say_hello() с двумя аргументами
say_hello(14, 'Елена')
# Будет напечатано: Добрый день, Елена!

# Забудем передать второй аргумент. Никаких имён!
say_hello(20)
# Будет напечатано: Добрый вечер!

# Функция не увидела второго аргумента 
# и присвоила переменной name значение '' (пустая строка)
# Сработало условие if name == '' и напечаталась строка без запятой и без name
