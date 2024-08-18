import csv
from typing import List

from csv_to_sql.models.basic_settings import BasicSettings


def parse_csv(file_path: str) -> List[BasicSettings]:
    data = []
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(BasicSettings(**row))
    print(data)
    return data
