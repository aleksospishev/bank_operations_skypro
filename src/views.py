import os
from datetime import datetime
from dotenv import load_dotenv
from src.utils import read_file_xlsx

load_dotenv()
PATH_FILE = os.getenv("PATH_TO_FILE_OPERATIONS")


def greeting(time_date: str):
    time = datetime.strptime(time_date, "%Y-%m-%d %H:%M:%S")
    if time.hour < 6:
        message = "Доброй ночи"
    elif time.hour < 12:
        message = "Доброе утро"
    elif time.hour < 18:
        message = "Добрый день"
    else:
        message = "Добрый вечер"
    return message


print(read_file_xlsx("data_test/test.xlsx"))

