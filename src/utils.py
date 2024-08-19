import logging
from typing import Any, Dict, List

import pandas as pd

utils_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def read_file_xlsx(path_file:str) -> list[dict[str, Any]]:
    utils_logger.info(f"Считываем данные из {path_file}")
    try:
        df = pd.read_excel(path_file)
        df = df.fillna("")
        return df.to_dict(orient="records")
    except FileNotFoundError as e:
        utils_logger.warning(e)
        return "Файл не найден"

# read_file_xlsx("../data/operations.xlsx")