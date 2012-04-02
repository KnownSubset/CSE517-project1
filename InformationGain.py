__author__ = 'nathan'
from sets import Set
from math import log

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
        for entropyOfClassifier in entropyByClassifiers[classifier].values():
            infoGain[classifier] = infoGain[classifier] - entropyOfClassifier
    return infoGain

def getTotalLengthOfData(data):
    totalCount = 0
    for element in data:
        totalCount += data[element].__len__()
    return totalCount


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
        lessThanTotal = greaterThanTotal = 0
        for classifier in subSequenceRange:
            range_classifier = subSequenceRange[classifier]
            value = range_classifier* 1.0 / lessThanCount
            if value > 0:
                lessThanTotal -= value*log(value, 2)
            value = (greaterThanCount - range_classifier) / (greaterThanCount * 1.0)
            if value > 0:
                greaterThanTotal -= value *log(value, 2)
        results[subSequence] = {'<':lessThanTotal*lessThanCount/totalCount, '>':greaterThanTotal*greaterThanCount/totalCount}
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