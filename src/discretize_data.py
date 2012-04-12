__author__ = 'nathan'

def read_in(fileName):
    f = open(fileName, 'r+')
    rows = []
    for line in f:
        row = []
        for cell in line.split(","):
            row.append(cell)
        rows.append(row)
    return rows

def read_in2(fileName):
    f = open(fileName, 'r+')
    rows = []
    for line in f.readline().split("\r"):
        row = []
        for cell in line.split("\t"):
            row.append(cell)
        rows.append(row)
    return rows


def discretize_row(discreteFilters, row, rowHeader):
    cells = []
    for cell in row:
        if not cell == 'NaN':
            cells.append(float(cell))
    mean = sum(cells) / len(cells)
    #mean = 0
    for cell in range(0,len(row)):
        if row[cell] == 'NaN':
            row[cell] = mean
        row[cell] = float(row[cell])
    filterValue = discreteFilters[rowHeader]
    for cell in range(0,len(row)):
        row[cell] = str(row[cell] < filterValue)
    return row


def discrete(fileName, discreteFileName):
    rows = read_in(discreteFileName)
    discreteFilters = dict()
    for row in rows:
        row[1] = float(row[1].replace('\'',''))
        row[0] = row[0].replace('\'','')
        row[0] = row[0].replace('(','')
        discreteFilters[row[0]] = row[1]
    data = read_in2(fileName)
    csv_file = open('/tmp/workfile', 'w')
    csv_file.write(",".join(data[0]) + "\n")
    for row in data[1:len(data)]:
        row[1:161] = discretize_row(discreteFilters, row[1:161], row[0])
        row[161:len(row)] = discretize_row(discreteFilters, row[161:len(row)], row[0])
        csv_file.write(",".join(row) + "\n")
    return rows