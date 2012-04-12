__author__ = 'nathan'

def transpose(rows):
    clone = []
    for row in range(0,rows[0].__len__()):
        clone.append([])
    for row in range(0,rows.__len__()):
        for column in range(0, rows[row].__len__()):
            clone[column].append(rows[row][column])
    return clone


def transpose_tsv_file(fileName):
    f = open(fileName, 'r+')
    rows = []
    for line in f.readline().split("\r"):
        row = []
        for cell in line.split("\t"):
            row.append(cell)
        rows.append(row)

    csv_file = open('/tmp/workfile', 'w')
    for row in transpose(rows):
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

    csv_file = open('/tmp/workfile', 'w')
    for row in transpose(rows):
        csv_file.write(",".join(row) + "\n")
    return rows