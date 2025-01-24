#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
#свариться на символ —— , як правильно треба було це вирішити?
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where - " said Alice.\n'  # Замінено довге тире на дефіс
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"- so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
# task 03 == Виведіть змінну alice_in_wonderland на друк
print("Task_01, Task_02, Task_03\n"
      f"Рішення: {alice_in_wonderland}\n"
      "__________________________________________________________________________________________"
      )

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
blackseasquare = 436402
azovseasquare = 37800
total_sea_square = blackseasquare + azovseasquare
task_04 = (
    "Task_04\n"
    f"Площа Чорного моря становить {blackseasquare}, а площа Азовського\n"
    f"моря становить {azovseasquare}. Яку площу займають Чорне та Азов-\n"
    f"ське моря разом?"
)
print(task_04)
print(f"Відповідь: {total_sea_square}\n"
      "__________________________________________________________________________________________")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
first_second = 250449
second_third = 222950
total_goods = 375291
first_goods = total_goods - second_third
second_goods = total_goods - first_second
third_goods = total_goods - first_goods
task_05 = (
    "Task_05\n"
    "Мережа супермаркетів має 3 склади, де всього розміщено\n"
    f"{total_goods} товар. На першому та другому складах перебуває\n"
    f"{first_second} товарів. На другому та третьому – {second_third} товарів.\n"
    "Знайдіть кількість товарів, що розміщені на кожному складі."
)
print(task_05)
print(f"Відповідь: на першому складі - {first_goods} товар,\n"
                  f"на другому складі - {second_goods} товари,\n"
                  f"на третьому складі - {third_goods} товарів.\n"
                  "__________________________________________________________________________________________")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
payment_period = 1.5
total_cost = monthly_payment * payment_period
task_06 = (
    "Task_06\n"
    "Михайло разом з батьками вирішили купити комп’ютер, ско-\n"
    "риставшись послугою «Оплата частинами». Відомо, що сплачу-\n"
    f"вати необхідно буде півтора року по {monthly_payment} грн/місяць. Обчисліть\n"
    "вартість комп’ютера."
)
print(task_06)
print(f"Відопідь: вартість комп'ютера складає {total_cost} грн\n"
      "__________________________________________________________________________________________")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
task_07 = (
    "Task_07\n"
    "Знайди остачу від діленя чисел:\n"
    "a) 8019 : 8     d) 7248 : 6\n"
    "b) 9907 : 9     e) 7128 : 5\n"
    "c) 2789 : 5     f) 19224 : 9"
)
print(task_07)
print("Відповідь: \n"
    f"a) {a}     d) {d}\n"
    f"b) {b}     e) {e}\n"
    f"c) {c}     f) {f}\n"
    "__________________________________________________________________________________________")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 4
pizza_medium = 2
juice = 4
cake = 1
water = 3
pizza_big_price = 274
pizza_medium_price = 218
juice_price = 35
cake_price = 350
water_price = 21
total_price = pizza_big * pizza_big_price + pizza_medium * pizza_medium_price + juice * juice_price + cake * cake_price + water * water_price
task_08 = (
    "Task_08\n"
    "Іринка, готуючись до свого дня народження, склала список того,\n"
    "що їй потрібно замовити. Обчисліть, скільки грошей знадобиться\n"
    "для даного її замовлення.\n"
    "Назва товару    Кількість        Ціна\n"
    f"Піца велика     {pizza_big}                {pizza_big_price} грн\n"
    f"Піца середня    {pizza_medium}                {pizza_medium_price} грн\n"
    f"Сік             {juice}                {juice_price} грн\n"
    f"Торт            {cake}                {cake_price} грн\n"
    f"Вода            {water}                {water_price} грн"
)
print(task_08)
print(f"Відповідь: загалом знадобиться {total_price} грн\n"
      "__________________________________________________________________________________________")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photoes = 232
photoes_per_page = 8
pages = photoes // photoes_per_page
if photoes % photoes_per_page:
    pages += 1 
task_09 = (
    "Task_09\n"
    f"Ігор займається фотографією. Він вирішив зібрати всі свої {photoes}\n"
    "фотографії та вклеїти в альбом. На одній сторінці може бути\n"
    f"розміщено щонайбільше {photoes_per_page} фото. Скільки сторінок знадобиться\n"
    "Ігорю, щоб вклеїти всі фото?"
)
print(task_09)
print(f"Відовідь: щоб вклеїти всі фото, знадобиться {pages}\n"
      "__________________________________________________________________________________________")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_per_100km = 9
tank_capacity = 48
fuel_needed = distance / 100 * fuel_per_100km
refills = fuel_needed // tank_capacity
if fuel_needed % tank_capacity:
    refills += 1
task_10 = (
    "Task_10\n"
    "Родина зібралася в автомобільну подорож із Харкова в Буда-\n"
    f"пешт. Відстань між цими містами становить {distance} км. Відомо,\n"
    f"що на кожні 100 км необхідно {fuel_per_100km} літрів бензину. Місткість баку\n"
    f"становить {tank_capacity} літрів.\n"
    "1) Скільки літрів бензину знадобиться для такої подорожі?\n"
    "2) Скільки щонайменше разів родині необхідно заїхати на зап-\n"
    "равку під час цієї подорожі, кожного разу заправляючи пов-\n"
    "ний бак?"
)
print(task_10)
print(f"Відповідь: для такої подорожі знадобиться {fuel_needed} л бензину.\n"
      f"Доведеться {refills} разів заїхати на заправку\n"
      "__________________________________________________________________________________________")

