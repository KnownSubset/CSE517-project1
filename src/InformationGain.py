__author__ = 'nathan'
from sets import Set
from math import log

def calculate_info_gain(columnMap):
    gains = []
    for attribute in columnMap:
        entropy = informationGain(columnMap[attribute])
        elements = sorted(entropy.values(), reverse=True)[0]
        for key in entropy.keys():
            if entropy[key] != elements:
                entropy.__delitem__(key)
            else:
                gains.append((attribute, key, elements))
    gains = sorted(gains, key=lambda gene: gene[2], reverse=True)
    for gain in gains:
        print gain


def calculate(file):
    f = open('/Users/nathan/Development/CSE517/project1/data.txt', 'r+')
    columnMap = dict()
#    for column in f.readline().split("\t"):
#        if not column in columnMap.keys():
#            columnMap[column] = []
#        columnMap[column].append()
#        count += 1
#    count = 0
    names = []
    first = True
    for line in f.readline().split("\r"):
        if first:
            first = False
            continue
        count = 0
        name = ""
        sumA = sumC = 0.0
        nans = []
        for cell in line.split("\t"):
            if count > 0:
                key = "A" if count < 161 else "C"
                if cell == "NaN":
                    nans.append(count)
                    value = count
                else:
                    value = float(cell)
                    if count < 161:
                        key = "A"
                        sumA += value
                    else:
                        key = "C"
                        sumC += value
                columnMap[name][key].append(value)
            else:
                name = cell
                columnMap[cell] = {"A":[], "C":[]}
                names.append(cell)
            count += 1
        def lt_filter(x): return x < 161
        def gt_filter(x): return x > 160
        lessThanFilter = filter(lt_filter, nans)
        greaterThanFilter = filter(gt_filter, nans)
        for nan in lessThanFilter:
            columnMap[name]['A'][nan-1] = sumA/ (160 - lessThanFilter.__len__())
        for nan in greaterThanFilter:
            columnMap[name]['C'][nan-161] = sumC/ (170 - greaterThanFilter.__len__())
    calculate_info_gain(columnMap)

def informationGain(dataPoints):
    totalCount = getTotalLengthOfData(dataPoints)
    entropy = 0
    for classifier in dataPoints:
        count = dataPoints[classifier].__len__()*1.0 / totalCount
        entropy -= count * log(count, 2.0)
    entropyByClassifiers = entropyIn(dataPoints)
    infoGain = dict()
    for classifier in entropyByClassifiers:
        infoGain[classifier] = entropy
    for classifier in entropyByClassifiers:
        for entropyOfClassifier in entropyByClassifiers[classifier].values()[0]:
            infoGain[classifier] = infoGain[classifier] - entropyOfClassifier
    return infoGain

def getTotalLengthOfData(data):
    totalCount = 0
    for element in data:
        totalCount += data[element].__len__()
    return totalCount


def entropy_for_greater_than(countOfClassificationInRange, classificationRange):
    value = countOfClassificationInRange * 1.0 / classificationRange
    otherValue = (classificationRange - countOfClassificationInRange) * 1.0 / classificationRange
    return -(value * log(value, 2) if value > 0 else 0)  - (otherValue * log(otherValue, 2) if otherValue > 0 else 0)

def entropy_for_less_than(countOfClassificationInRange, classificationRange):
    value = countOfClassificationInRange * 1.0 / classificationRange
    otherValue = (classificationRange - countOfClassificationInRange) * 1.0 / classificationRange
    return -(value * log(value, 2) if value > 0 else 0)  - (otherValue * log(otherValue, 2) if otherValue > 0 else 0)

def entropyIn(data):
    subSequences = classification(data)
    results = dict()
    totalCount = getTotalLengthOfData(data)
    for subSequence in subSequences:
        subSequenceRange = subSequences[subSequence]
        lessThanCount = 0
        for classifier in subSequenceRange:
             lessThanCount += subSequenceRange[classifier]
        greaterThanCount = totalCount - lessThanCount
        results[subSequence] = dict()
        for classifier in subSequenceRange:
            countOfClassificationInRange = subSequenceRange[classifier]
            results[subSequence][classifier] = [(float(lessThanCount)/totalCount)*entropy_for_less_than(countOfClassificationInRange, lessThanCount)]
        for classifier in subSequenceRange:
            countOfClassificationInRange = subSequenceRange[classifier]
            classificationSize = data[classifier].__len__()
            results[subSequence][classifier].append((greaterThanCount*1.0/totalCount)*entropy_for_greater_than(classificationSize - countOfClassificationInRange, greaterThanCount))
    return results



def discretize(dataPoints):
    values = sorted(Set(dataPoints))
    discreteValues = dict()
    for i in range(values.__len__() - 1):
        discreteValues[(values[i] + values[i+1])/2.0] = i+1
    return discreteValues


def classification(dataPoints):
    allDatapoints = []
    for classifier in dataPoints:
        allDatapoints.extend(dataPoints[classifier])
    discreteValues = discretize(allDatapoints)
    results = dict()
    for  discreteValue in discreteValues:
        results[discreteValue] = dict()
        for classifier in dataPoints:
            results[discreteValue][classifier] = 0
    for classifier in dataPoints:
        for value in dataPoints[classifier]:
            for  discreteValue in discreteValues:
                if value < discreteValue:
                    results[discreteValue][classifier] += 1
    return results