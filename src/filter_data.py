__author__ = 'nathan'

def filter_data(fileName, filters):
    f = open(fileName, 'r+')
    rows = []
    for line in f.readline().split("\r"):
        row = []
        for cell in line.split("\t"):
            row.append(cell)
        if row[0] in filters:
            rows.append(row)

    csv_file = open('/tmp/workfile', 'w')
    for row in rows:
        csv_file.write(",".join(row) + "\n")
    return rows