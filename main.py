from collections import defaultdict
from calendar import day_name
from datetime import datetime
from typing import List, Dict, Optional, Union, Tuple
import sys

TODAY = datetime.today().date()
CONTACTS = {}


def _convert_user_birthday_to_current_year(users: List[Dict[str, Union[str, datetime]]]) \
        -> List[Dict[str, Union[str, datetime]]]:
    return [{"name": user.get("name"), "birthday": user.get("birthday").date().replace(year=TODAY.year)} for user in
            users]


def _estimate_birthday_delta(user: Dict[str, Union[str, datetime]]) -> Optional[str]:
    delta_days = (user.get("birthday") - TODAY).days
    if delta_days < 7:
        return user.get("birthday").strftime("%A")


def _parse_input(user_input: str) -> Tuple[str, ...]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def get_birthdays_per_week(users: List[Dict[str, Union[str, datetime]]]) -> None:
    users_with_day_this_week = defaultdict(list)
    updated_users_list = _convert_user_birthday_to_current_year(users)

    for user in updated_users_list:
        if day := _estimate_birthday_delta(user):
            if day.lower() in ["saturday", "sunday"]:
                users_with_day_this_week["Monday"].append(user.get("name"))
            else:
                users_with_day_this_week[day].append(user.get("name"))

    sorted_days = sorted(users_with_day_this_week.keys(), key=lambda x: list(day_name).index(x))

    for day in sorted_days:
        print(f"{day}: {', '.join(users_with_day_this_week[day])}")


def _add_contact(*args) -> str:
    if len(args) != 2:
        return "Invalid number of arguments for add command, please try again."

    name, phone = args

    if name in CONTACTS:
        change = input(f"Contact {name.capitalize()} already exists. Do you want to change it?")
        if change.lower() in ["yes", "y"]:
            return _change_contact(name, phone)
        else:
            _hello_bot()
    else:
        CONTACTS[name] = phone
        return f"Contact {name.capitalize()} has been added."


def _change_contact(*args) -> str:
    if len(args) != 2:
        return "Invalid number of arguments for add command, please try again."
    name, phone = args

    if name not in CONTACTS:
        return f"Contact {name.capitalize()} does not exist."
    else:
        CONTACTS[name] = phone
        return f"Contact {name.capitalize()} has been updated."


def _get_all() -> None:
    for name, phone in CONTACTS.items():
        print(f"{name.capitalize()}:\t {phone}")


def _get_phone(*args) -> str:
    if len(args) != 1:
        return "Invalid number of arguments for phone command, please try again."
    name = args[0]
    if name not in CONTACTS:
        return f"Contact {name.capitalize()} does not exist."
    else:
        return f"{name.capitalize()}: {CONTACTS[name]}"


def _exit_bot() -> str:
    return "Goodbye!"


def _hello_bot() -> str:
    return "How can I help you?"


SUPPORTED_COMMANDS = {"exit": _exit_bot,
                      "close": _exit_bot,
                      "hello": _hello_bot,
                      "add": _add_contact,
                      "change": _change_contact,
                      "phone": _get_phone,
                      "all": _get_all
                      }


def bot_event_loop():
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ").strip().lower()
            command, *args = _parse_input(user_input)
            result = SUPPORTED_COMMANDS[command](*args)
            if result:
                print(result)
        except KeyError:
            print(f"Invalid command, supported commands are:")
            for key in SUPPORTED_COMMANDS.keys():
                print(f" - {key}")
            print("Please try again.")
        except KeyboardInterrupt:
            print("Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    bot_event_loop()
