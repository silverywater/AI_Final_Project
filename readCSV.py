import csv

def readCSV(filename):
    file = open(filename, 'r')
    csvFile = csv.reader(file)
    map = []
    for row in csvFile:
        mapRow = []
        for item in row:
            if item.isnumeric():
                mapRow.append(int(item))
            else:
                mapRow.append(item)
        map.append(mapRow)
    return map
