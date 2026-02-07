from datetime import date, datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.02.07"},
    {"name": "Jane Smith", "birthday": "1990.02.13"},
]


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]] | list:
    upcoming_users_birthday = []
    days_ahead = 7
    current_date = date.today()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=current_date.year)

        delta_days = (birthday_this_year - current_date).days

        is_upcoming = 0 <= delta_days <= days_ahead

        should_shift_to_next_year = birthday_this_year < current_date

        if should_shift_to_next_year:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        if is_upcoming:
            is_saturday = birthday_this_year.weekday() == 5  # Saturday
            is_sunday = birthday_this_year.weekday() == 6  # Sunday

            if is_saturday:
                birthday_this_year += timedelta(days=2)
            elif is_sunday:
                birthday_this_year += timedelta(days=1)

            upcoming_users_birthday.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_users_birthday


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
