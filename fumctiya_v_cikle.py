def print_money_count(money_count):
    remainder = money_count % 10
    if money_count == 0:
        print('У тебя нет денег')
    elif remainder == 0 or remainder >= 5 or (10 <= money_count <= 19):
        print('У тебя', money_count, 'рублей')
    elif remainder == 1:
        print('У тебя', money_count, 'рубль')
    else:
        print('У тебя', money_count, 'рубля')
for i in range(1,11):
    print_money_count(i)
