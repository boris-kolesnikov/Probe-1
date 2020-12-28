def print_friends_count(friends_count):
    remainder = friends_count % 10
    if friends_count == 0:
        print('У тебя нет денег')
    elif remainder == 0 or remainder >= 5 or (10 <= friends_count <= 19):
        print('У тебя', friends_count, 'рублей')
    elif remainder == 1:
        print('У тебя', friends_count, 'рубль')
    else:
        print('У тебя', friends_count, 'рубля')
for i in range(1,11):
    print(print_friends_count(i))
