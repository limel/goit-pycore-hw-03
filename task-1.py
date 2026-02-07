from datetime import datetime


def get_days_from_today(date: str) -> int | str:
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Невірний формат дати. Використовуйте 'РРРР-ММ-ДД'"

    today = datetime.today().date()
    delta = today - target_date
    return delta.days


print(get_days_from_today("2026-02-05"))
print(get_days_from_today("2024-10-20"))  # Приклад виклику функції з минулою датою
print(get_days_from_today("2026-10-08"))  # Приклад виклику функції з майбутньою датою
print(get_days_from_today("20.10.2020"))  # Неправильний формат дати
