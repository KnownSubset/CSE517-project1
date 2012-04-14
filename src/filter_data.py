import discretize_data
import tranpose_csv

__author__ = 'nathan'

def read_in_file(fileName):
    f = open(fileName, 'r+')
    rows = []
    for line in f.readline().split("\r"):
        row = []
        for cell in line.split(","):
            row.append(cell)
        rows.append(row)
    return rows

def read_in_filters(fileName, count):
    f = open(fileName, 'r+')
    rows = []
    for line in f:
        row = line.split(",")
        rows.append(row[0].replace("(","").replace(")","").replace("'",""))
    return rows[0:count]

def filter_file_using_filtered_file(fileName, filterFile, count):
    filters = read_in_filters(filterFile, count)
    return filter_file(fileName, filters)

def filter_file(fileName, filters):
    csv_file = open(fileName+'.filtered', 'w')
    rows = read_in_file(fileName)
    filteredRows = filter_data(rows, filters)
    filteredRows.insert(0, rows[0])
    for row in filteredRows:
        csv_file.write(",".join(row) + "\n")
    return rows

def filter_data(rows, filters):
    newRows = []
    for row in rows:
        if row[0] in filters:
            newRows.append(row)
    return newRows


def process_file(dataFileName, filterFileName, count):
    filters = read_in_filters(filterFileName, count)
    rows = read_in_file(dataFileName)
    filteredRows = filter_data(rows, filters)
    filteredRows.insert(0, rows[0])
    data = discretize_data.discretize_data(filteredRows, filterFileName)
    data = tranpose_csv.transpose(data)
    csv_file = open('/Users/nathan/Development/CSE517/project1/workfile_zero_'+str(count)+'.csv', 'w')
    for row in data:
        csv_file.write(",".join(row) + "\r\n")
    return None
