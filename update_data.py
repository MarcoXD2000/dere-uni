import json
import csv

def unit_construct(unit, members):
    new_unit = {unit : members}
    return new_unit

def idol_construct(idol, units):
    new_idol = {idol : units}
    return new_idol

def idol_data_construct(name, color, type):
    new_idol = {name : {"screenName" : name, "color" : color, "type" : type}}
    return new_idol

def unit_normalize(name):
    unit_normal = {name:name}
    return unit_normal

def read_csv(filename:str):
    with open(filename, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        string = []
        for line in reader:
            string.append(line)
        return string

#unitToIdol
datas = read_csv(".\src\data\\unit2idol.csv")

data_json = {}
unit_normal_json = {}

for data in datas:
    data[1] = data[1].split('_')
    unit = unit_construct(data[0],data[1])
    data_json.update(unit)
    unit_normal_json.update(unit_normalize(data[0]))

with open('.\src\data\\unitToIdol.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_json, outfile, ensure_ascii=False, indent=4)
    outfile.close()

with open('.\src\data\\unitNormalize.json', 'w', encoding='utf-8') as outfile:
    json.dump(unit_normal_json, outfile, ensure_ascii=False, indent=4)
    outfile.close()

# idolToUnit
idol_list = []
total_idol = 0
total_unit = 0
for data in datas:
    total_unit = total_unit + 1
    for idol in data[1]:
        if idol not in idol_list:
            idol_list.append(idol)
            total_idol = total_idol + 1


data_json = {}
idols_unit = []
for i in range(total_idol):
    idols_unit.append([])

for data in datas:
    for idol in data[1]:
        idol_unit = []

        idols_unit[idol_list.index(idol)].append(data[0])


for idol in idol_list:
    add_idol = idol_construct(idol, idols_unit[idol_list.index(idol)])
    data_json.update(add_idol)



with open('.\src\data\idolToUnit.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_json, outfile, ensure_ascii=False, indent=4)
    outfile.close()

#idolData
data_json = {}
datas = read_csv(".\src\data\idolData.csv")
firstline = True
for data in datas:
    if firstline:
        firstline = False
        continue
    idol = idol_data_construct(data[0], data[1], data[2])
    data_json.update(idol)

with open('.\src\data\idolData.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_json, outfile, ensure_ascii=False, indent=4)
    outfile.close()


#idolIcon
icon_csv = read_csv(".\\src\\styles\\idolIcon.csv")

# .idolIcon-天海春香 {
#   background-image: url("https://millionlive-theaterdays.idolmaster-official.jp/assets/img/idol/thumb/1/thumb.jpg");
#}
icon_string = ""

for url in icon_csv:
    icon_string = icon_string + ".idolIcon-" + url[0] + " {\n"
    icon_string = icon_string + '   background-image: url("' + url[1] + '");\n'
    icon_string = icon_string + "}\n"

with open(".\\src\\styles\\idolIcon.css", "w", encoding='utf-8') as f:
    f.write(icon_string)
    f.close()