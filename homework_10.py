# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть.
import random
print('0 - Герб | 1 - Решка')
mycoins = [random.randint(0, 1) for _ in range(20)]
print(mycoins)
count_zero = 0
count_one = 0
for i in mycoins:
    if i == 0:
        count_zero += 1
    else:
        count_one += 1

print(f"Вверх гербом: {count_zero}")
print(f"Вверх решкой: {count_one}\n")

if count_zero < count_one:
    print(
        f"Кол-во монет лежащих вверх гербом: ({count_zero}) что меньше кол-ва монет лежащих вверх решкой ({count_one})")
    print(f"Перевернули {count_zero} шт. с Гербом!")
elif count_zero == count_one or count_one == count_zero:
    print(
        f"Количество перевернутых монет одинаково! Можно перевернуть {count_one} шт. с Гербом или Решкой.")
    print(f"Перевернули ({count_zero}) монет.")

else:
    print(
        f"Кол-во монет лежащих вверх гербом: ({count_zero}) что больше кол-ва монет лежащих вверх решкой ({count_one})")
    print(f"Перевернули {count_one} шт. с Решкой!")


print(f"Всего монет на столе: {count_one + count_zero}")
