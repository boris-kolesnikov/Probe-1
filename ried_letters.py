messages_count = 11
for i in reversed(range(2, messages_count)):
    print('- Анфиса, есть ли новые письма?')
    print('- Непрочитанных писем:', str(i))
    print('Я прочитал одно, и их осталось', str(i-1))
# После выполнения цикла напечатать завершающие строки:
print('- Анфиса, есть ли новые письма?')
print('- Одно непрочитанное письмо')
print('Я прочитал его. И нет больше писем!')
