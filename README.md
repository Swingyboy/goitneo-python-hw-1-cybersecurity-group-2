# Console Assistant Bot

Welcome to the Assistant Bot project! This bot helps users manage their contacts by allowing them to add, change, or retrieve phone numbers. It provides a simple command-line interface for interacting with the bot.

## Features

- Add new contacts with their phone numbers
- Change existing contact phone numbers
- Retrieve phone numbers for specific contacts
- View all contacts and their phone numbers
- Greet users and provide assistance

## Getting Started

To use the Assistant Bot, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure you have Python installed on your system. This project is compatible with Python 3.10
4. Run the bot:
   ```python console_bot.py```
   
5. Follow the on-screen instructions to interact with the bot.
 
## Usage

Once the bot is running, you can enter commands to manage your contacts. Here are the supported commands:

 - **add** <name> <phone>: Add a new contact with the given name and phone number.
 - **change** <name> <phone>: Change the phone number of an existing contact.
 - **phone** <name>: Retrieve the phone number of a specific contact.
 - **all**: View all contacts and their phone numbers.
 - **hello**: Greet the bot and get assistance.
 - **exit** or **close**: Exit the bot.
 
 
# get_birthday_per_week Function

The `get_birthdays_per_week` function prints users whose birthday is next week.

## Function Signature

```python
def get_birthdays_per_week(users: List[Dict[str, Union[str, datetime]]]) -> None:
    pass
```

## Parameters
 - **users**: A list of dictionaries containing user information. Each dictionary should have a "name" key (string) representing the user's name and a "birthday" key (datetime) representing the user's birthday.    

## Return Value
This function does not return anything (None). It prints prints users whose birthday is next week.

## Example Usage

```
from your_module import get_birthdays_per_week

users = [
    {"name": "Alice", "birthday": datetime(1990, 3, 15)},
    {"name": "Bob", "birthday": datetime(1985, 5, 20)},
    {"name": "Charlie", "birthday": datetime(1995, 7, 25)},
    {"name": "David", "birthday": datetime(1980, 9, 10)},
    {"name": "Eve", "birthday": datetime(1992, 11, 30)}
]

get_birthdays_per_week(users)
```
