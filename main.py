from collections import defaultdict
from calendar import day_name
from datetime import datetime
from typing import List, Dict, Optional, Union

TODAY = datetime.today().date()


def _convert_user_birthday_to_current_year(users: List[Dict[str, Union[str, datetime]]]) \
        -> List[Dict[str, Union[str, datetime]]]:
    return [{"name": user.get("name"), "birthday": user.get("birthday").date().replace(year=TODAY.year)} for user in
            users]


def _estimate_birthday_delta(user: Dict[str, Union[str, datetime]]) -> Optional[str]:
    delta_days = (user.get("birthday") - TODAY).days
    if delta_days < 7:
        return user.get("birthday").strftime("%A")


def get_birthdays_per_week(users: List[Dict[str, Union[str, datetime]]]) -> None:
    users_with_day_this_week = defaultdict(list)
    updated_users_list = _convert_user_birthday_to_current_year(users)

    for user in updated_users_list:
        if day := _estimate_birthday_delta(user):
            if day.upper() in ["SATURDAY", "SUNDAY"]:
                users_with_day_this_week["Monday"].append(user.get("name"))
            else:
                users_with_day_this_week[day].append(user.get("name"))

    sorted_days = sorted(users_with_day_this_week.keys(), key=lambda x: list(day_name).index(x))

    for day in sorted_days:
        print(f"{day}: {', '.join(users_with_day_this_week[day])}")


if __name__ == "__main__":
    users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
             {"name": "Serhii Bezuhlyi", "birthday": datetime(1988, 4, 28)},
             {"name": "John Smith", "birthday": datetime(1965, 2, 9)},
             {"name": "Jack Smith", "birthday": datetime(1966, 2, 9)},
             {"name": "Jane Smith", "birthday": datetime(1965, 2, 11)},
             ]
    get_birthdays_per_week(users)
