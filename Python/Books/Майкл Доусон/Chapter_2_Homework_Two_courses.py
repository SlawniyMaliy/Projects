# Два блюда
# Программа спрашивает у пользователя два любимых блюда и делает конкатенирует

print("Если вы назовете два своих любимых блюда, то повар сделает " \
     + "\"Шедевер\" под ваши вкусовые предпочтения")
like_dish_1 = input("\nНазовите первое любимое блюдо: ")
like_dish_2 = input("Назовите второе любимое блюдо: ")

print("\nПараааам, а вот и сюрприз!!! Специально для вас Шеф-повар приготовил на кухне",
      '"' + like_dish_1.title() + like_dish_2.lower() + '"!')