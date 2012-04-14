__author__ = 'nathan'

def transpose(rows):
    clone = []
    for row in range(0,len(rows[0])):
        clone.append([])
    for row in range(0,len(rows)):
        for column in range(0, len(rows[row])):
            clone[column].append(rows[row][column].replace("\n",""))
    return clone


def transpose_tsv_file(fileName):
    f = open(fileName, 'r+')
    rows = []
    for line in f:
        row = []
        for cell in line.split("\t"):
            row.append(cell.replace("\n",""))
        rows.append(row)

    csv_file = open(fileName+'.csv', 'w')
    transpose1 = transpose(rows)
    for row in transpose1:
        csv_file.write(",".join(row) + "\n")
    return rows

def transpose_file(fileName):
    f = open(fileName, 'r+')
    rows = []
    for line in f:
        row = []
        for cell in line.split(","):
            row.append(cell)
        rows.append(row)

    csv_file = open('/Users/nathan/Development/CSE517/project1/workfile.csv', 'w')
    transposedRows = transpose(rows)
    for row in transposedRows:
        csv_file.write(",".join(row) + "\r\n")
    return rows