# Орел и решка
# Программа рандомно подбрасывает монету 100 раз
import random

num = 100
eagle = 0
tails = 0

print("Предлагаю сыграть в игру 'Орел и решка'!")
press = input("Если вы готовы сыграть, нажмите латинскую букву 'Y' в противтом случае 'N' если нет: ")

while press.upper() != 'Y' and press.upper() != 'N':
    press = input("Не совсем понял Ваш выбор, нажмите латинскую букву Y или N: ")
    
if press.upper() == 'Y':
    #print("Вам достался пирожок с", surprise)
    while num > 0:
        result = random.randint(0, 1)
        if result == 0:
            eagle += 1
        else:
            tails += 1
        num -= 1
    print("Орёл выпал:", eagle, "раз", "\nРешка выпала:", tails, "раз")
elif  press.upper() == 'N':
    print("Как хотите! Будем Вас ждать в другой раз!")

