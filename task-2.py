import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1:
        print(f"Помилка: мінімальне число повинно бути не менше 1 (отримано {min}).")
        return []

    if max > 1000:
        print(
            f"Помилка: максимальне число повинно бути не більше 1000 (отримано {max})."
        )
        return []

    if min > max:
        print(
            f"Помилка: мінімальне число ({min}) не може бути більше максимального ({max})."
        )
        return []

    available_numbers = max - min + 1
    if quantity < 1 or quantity > available_numbers:
        print(
            f"Помилка: кількість чисел повинна бути від 1 до {available_numbers} (отримано {quantity})."
        )
        return []

    numbers_range = range(min, max + 1)
    random_numbers = random.sample(numbers_range, quantity)
    winning_numbers = sorted(random_numbers)

    return winning_numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
print(get_numbers_ticket(0, 50, 6))  # min < 1
print(get_numbers_ticket(1, 1001, 6))  # max > 1000
print(get_numbers_ticket(10, 5, 3))  # min > max
print(get_numbers_ticket(1, 10, 15))  # quantity > available_numbers
