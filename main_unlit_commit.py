задача = 'Квадратное уравнение — это уравнение вида ax^2 + bx + c = 0. ' # Здесь пример в целом
print (задача)

print ('Для решения введите последовательно коэффициенты a, b, c') # И требуемые для его решения данные

print ("введите а и нажмите Enter"); a = int(input ())

print ("введите b и нажмите Enter"); b = int(input ())

print ("введите c и нажмите Enter"); c = int(input ())

D = b**2-4*a*c # Рассчет дискриминанта

print('дискриминант равен'); print(D)

if  D == 0: print ('уравнение имеет один корень, ответ: ');
x = -b/2*a; print(x)# Решение уравнения на основе дискриминанта

if D < 0: print ('уравнение не имеет ответа т.к. D<0')

if D > 0: print ('D>0, уравнение имеет два корня, x1 и x2');
x1=(-b+D**0.5)/(2*a); x2=(-b-D**0.5)/(2*a); print ('x1 ='); print(x1); print ('x2 ='); print(x2)
