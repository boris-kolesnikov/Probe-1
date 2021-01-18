def say_hello(name='', hello='Привет!'):
        if name!='':
                print(name, hello)
        elif name=='':
                print(hello)

def  avengers():
        say_hello("Сэм")
        say_hello("Гимли")
        say_hello("Гендальф")
        say_hello("Фродо")
        
avengers()

