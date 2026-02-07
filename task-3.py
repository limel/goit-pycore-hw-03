import re

PHONE_PREFIX = "+380"


def normalize_phone(phone_number: str) -> str:
    cleaned_number = re.sub(r"[^0-9+]", "", phone_number)
    correct_number = re.sub(r"^(?:\+?380|80|0)?", PHONE_PREFIX, cleaned_number)

    return correct_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "8050-111-22-22",
    "38050 111 22 11   ",
    "+380501112289   ",
    "8050223356",
    "501234567",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
