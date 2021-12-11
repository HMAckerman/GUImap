# ---------- XML TO CSV ----------
# import xml.etree.ElementTree as ET
# import csv

# print(str(fname))

# string1 = "This is a test string"
# string2 = "This is another test string"
# string3 = string1 + string2
# print(string3)

# tree = ET.parse("testfile.xml")
# root = tree.getroot()

# --------- XML TO JSON --------

import json
import xmltodict

with open("scan1.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

    json_data = json.dumps(data_dict)

    with open("scan.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()

# --------- JSON TO CSV ----------
# import json
# import csv

# with open('scan.json') as json_file:
#     data = json.load(json_file)

# scan_data = data['nmaprun']

# data_file = open('scan_file.csv', 'w')

# csv_writer = csv.writer(data_file)

# count = 0

# for results in scan_data:
#     if count == 0:
#         header = scan_data[results].keys()
#         csv_writer.writerow(header)
#         count += 1

#     csv_writer.writerow(results.values())
# data_file.close()


# # ---------- JSON TO CSV (SECOND METHOD) ---------
import json
import csv

with open('scan.json') as json_file:
    jsondata = json.load(json_file)

data_file = open('scanresults.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0
for data in jsondata:
    if count == 0:
        header = jsondata[data].keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(jsondata[data].values())

data_file.close()