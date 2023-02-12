# Автодилер
# Программа запрашивате стоимость автомобиля
# и выводит окончательную стоимость со всеми доплатами.

car_cost = int(input("Введите на какую стоимость автомобиля вы рассчитываете: "))
tax = car_cost * 0.2
regist_fee = car_cost * 0.33
agency_fee = 500
delivery = 200
total = car_cost + tax + regist_fee + agency_fee + delivery
print("Окончательная стоимость автомобиля:", '$' + str(int(total)))