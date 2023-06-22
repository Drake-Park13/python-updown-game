
from random import randrange

print('','1.easy','\n','2.normal','\n','3.hard','\n','4.custom','\n','5.exit')
num = int(input('번호를 선택 하세요:'))

if num == 1:
    print('easy game stat!')
    num = randrange(1,11)
    a = 0
    b = 0
    while a != num:
        a += 1
        b = int(input("1~10 숫자 입력: "))
        if b < num:
            print("UP")
        elif b > num:
            print("DOWN")
        else :
            print("정답입니다! {}회 만에 맞췄어요.".format(a))
            break

if num == 2:
    print('nornal game stat!')
    num = randrange(1,101)
    c = 0
    d = 0
    while c != num:
        c += 1
        d = int(input("1~100 숫자 입력: "))
        if d < num:
            print("UP")
        elif d > num:
            print("DOWN")
        else :
            print("정답입니다! {}회 만에 맞췄어요.".format(c))
            break
    
if num == 3:
    print('hard gmae start!')
    num = randrange(1,1001)
    e = 0
    f = 0
    while e != num:
        e += 1
        f = int(input("1~1000 숫자 입력: "))
        if f < num:
            print("UP")
        elif f > num:
            print("DOWN")
        else :
            print("정답입니다! {}회 만에 맞췄어요.".format(e))
            break

if num == 4:
    print('custom gmae start!')
    cs = int(input("1 부터 몇까지? : "))
    num = randrange(1,cs)
    e = 0
    f = 0
    while e != num:
        e += 1
        f = cs = int(input("1 부터 {}까지? : ".format(cs)))
        if f < num:
            print("UP")
        elif f > num:
            print("DOWN")
        else :
            print("정답입니다! {}회 만에 맞췄어요.".format(e))
            break

if num == 5:
    print('exit!')