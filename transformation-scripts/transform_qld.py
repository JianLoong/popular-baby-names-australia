import csv
import json
from turtle import pos
import jsonpickle


class Name:
    def __init__(self, position, name="", count=0, sex="", year=0):
        self.position = position
        self.name = name
        self.count = count
        self.sex = sex
        self.year = year

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)


def process(file_path, year):
    # page = reader.pages[page_number]
    # text = page.extract_text()
    names = []

    with open(file_path, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(rows)
        position = 1
        for columns in rows:

            if columns[0] != "":
                name = Name(position, columns[0], int(
                    columns[1]), "FEMALE", year)
                names.append(name)

            if columns[3] != "":
                name = Name(position, columns[2], int(
                    columns[3]), "MALE", year)
                names.append(name)

            position = position + 1

    with open(str(year) + ".json", "w") as outfile:
        outfile.write(jsonpickle.encode(names, unpicklable=False, indent=4))


file_path = 'raw\\qld\\bdm-top-100-baby-names-2019.csv'

year = 2019
process(file_path, year)
