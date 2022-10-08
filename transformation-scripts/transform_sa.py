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
    names = []

    with open(file_path, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(rows)
        position = 1
        for columns in rows:

            if columns[0] != "":
                name = Name(
                    int(columns[2].replace('"', "").replace('=',"")), 
                    columns[0].replace('"', ""), 
                    int(columns[1].replace('"', "").replace('=',"")), 
                    "MALE", year)
                names.append(name)

            # position = position + 1

    with open(str(year) + "male.json", "w") as outfile:
        outfile.write(jsonpickle.encode(names, unpicklable=False, indent=4))


file_path = 'C:\\Users\\Jian\\Desktop\\popular-baby-names-victoria\\raw\\sa\\male_cy2019_top100.csv'
year = 2019
process(file_path, year)
