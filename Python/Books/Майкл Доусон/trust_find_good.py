# Рантье (версия без ошибки)
# Демонстрирует type conversion
print(
"""
            Рантье
Программа подсчитывает выши ежемесячные расходы. Эту статистику нужно знать затем.
Чтобы у вас не кончились деньги и вам не пришлось искать работу.
Введите суммы расходов по всем статьям. Перечисляемым ниже. Вы богаты - так не ме-
лочитесь. Пошите суммы в долларах. без центов.
"""
)

car = input("Техническое обслуживание машины 'Ламборгини': ")
car = int(car)
rent = int(input("Сьем раскошной квартиры на Манхэттене: "))
jet = int(input("Аренда самолета: "))
gifts = int(input("Подарки: "))
food = int(input("Обеды и ужины в ресторанах: "))
staff = int(input("Жалованье прислуги (дворецкий, повар, водитель, секретарь): "))
guru = int(input("Плата личному психоаналитику: "))
games = int(input("Компьютерные игры: "))
total = car + rent + jet + gifts + food + staff + guru + games
print("\n\nОбщая сумма:", total)
input("\n\nНажмите Enter, чтобы выйти.")