from PyPDF2 import PdfReader
import json
import pprint

import jsonpickle

class Name:
    def __init__(self, position, name, count, sex, year):
        self.position = position
        self.name = name
        self.count = count
        self.sex = sex
        self.year = year

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)


file_path = 'C:\\Users\\Jian\\Desktop\\popular-baby-names-victoria\\raw\\nsw\\popular-baby-names-2000s.pdf'
# template_path = "C:\\Users\\Jian\\Desktop\\popular-baby-names-victoria\\transformation-scripts\\BDM_top-100-baby-names-2021.tabula-template.json"

reader = PdfReader(file_path)
number_of_pages = len(reader.pages)
page = reader.pages[1]
text = page.extract_text()

names = []

lines = text.split("\n")
lines.pop(0)
lines.pop(0)
# lines.pop(len(lines) - 1)
year = 2008
index = 1
for line in lines:
    columns = line.split(" ")
    # First column
    name = ''.join([i for i in columns[0] if not i.isdigit()])
    position = int(''.join([i for i in columns[0] if  i.isdigit()]))

    maleEntry = Name(position,name,int(columns[1]),"MALE", year)

    name = ''.join([i for i in columns[2] if not i.isdigit()])
    # position = ''.join([i for i in columns[2] if  i.isdigit()])
    femaleEntry =  Name(position,name, int(columns[3]),"FEMALE", year)
   

    names.append(maleEntry)
    names.append(femaleEntry)



    name = ''.join([i for i in columns[4] if not i.isdigit()])
    position = int(''.join([i for i in columns[4] if  i.isdigit()]))

    maleEntrySecond =  Name(position,name ,int(columns[5]),"MALE", year)

    name = ''.join([i for i in columns[6] if not i.isdigit()])

    femaleEntrySecond =  Name(position,name, int(columns[7]),"FEMALE", year)

    names.append(maleEntrySecond)
    names.append(femaleEntrySecond)

# for line in lines:
#     columns = line.split(" ")
#     # First column
#     # result = ''.join([i for i in s if not i.isdigit()])
#     maleEntry = Name(int(columns[0]),columns[1],int(columns[2]),"MALE", year)
#     femaleEntry =  Name(int(columns[0]),columns[3],int(columns[4]),"FEMALE", year)
#     # Second column

#     names.append(maleEntry)
#     names.append(femaleEntry)

#     maleEntrySecond =  Name(int(columns[5]),columns[6],int(columns[7]),"MALE", year)
#     femaleEntrySecond =  Name(int(columns[5]),columns[8],int(columns[9]),"FEMALE", year)

#     names.append(maleEntrySecond)
#     names.append(femaleEntrySecond)

# json_result = "["
# for index in range(0, len(names) - 1):
#    json_result += names[index].to_json()
#    if index != len(names) - 2:
#     json_result += ","
# json_result += "]"



with open("nsw-2008.json", "w") as outfile:
    outfile.write(jsonpickle.encode(names, unpicklable=False, indent=4))
