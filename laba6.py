import random
from random import randint

print('-'*50)
print('0 - выход из программы')
print('1 - нахвание функции №1')
print('2 - нахвание функции №2')
print('3 - нахвание функции №3')
print('4 - нахвание функции №4')
print('5 - нахвание функции №5')
print('-'*50)

def f1():
    print("Функция №1")
    a = ['gfgdg', 'afafafsafadsfa', 'sfagadgag', 'asfasf', 'qwerty','qqqeew', 'wswesw']
    for i in a:
        if len(i) < 10:
            print(i)
        else:
            continue
    print('-' * 50)
def f2():
    print("Функция №2")
    x = 'Мария купила 24 груши по 300 рублей за 10кг'
    y = []
    for i in x:
        if i.isalpha():
            y.append(i)
    print(''.join(y))

    print('-' * 50)
def f3():
    print("Функция №3")
    a = [randint(0, 100) for i in range(10)]
    print(*a)
    a.extend(randint(0, 50) for i in range(5))
    print(*a)
    print(*[i for i in a if i%2 !=0])
    print('-' * 50)
def f4():
    print("Функция №4")
    alphabet = 'аеёиоуыэыяюбвгджзйклмнпрстфхцчшщ'
    count = 0
    res = ''
    while count !=5:
         res+= random.choice(alphabet.upper())
         count += 1

    print(f'Случайные{count} символов:{res}')
    print('-' * 50)
def f5():
    print("Функция №5")
    base = [2, 4, 6, 'a', 10, 'asd', 1, 3, 4, 5, 15]
    text = []
    for elem in base:
        if isinstance(elem, int) and elem % 2 !=0:
            text += [elem]
    print(text)
    print('-' * 50)

while True:
    x = int(input())
    if x == 0:
        print('Завершение программы')
        break
    elif x == 1:
        f1()
    elif x == 2:
        f2()
    elif x == 3:
        f3()
    elif x == 4:
        f4()
    elif x == 5:
        f5()
    else:
        print('Некорректный ввод')

    y = input('Вы хотите продолжить если да нажмите "да,1,yes,Y",если хотите завершить нажмите "нет,0,no, N"')
    if y == "1" or y == 'yes' or y == 'Y' or y == 'да':continue

    if y == "0" or y == 'no' or y == 'N' or y == 'нет':
        print('exit')
        break

