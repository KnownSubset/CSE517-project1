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
        results[subSequence] = dict()
        for classifier in subSequenceRange:
            countOfClassificationInRange = subSequenceRange[classifier]
            classificationSize = data[classifier].__len__();
            results[subSequence][classifier+'<'] = entropy_for_less_than(countOfClassificationInRange, lessThanCount)
            results[subSequence][classifier+'>'] = entropy_for_greater_than(classificationSize - countOfClassificationInRange, totalCount - lessThanCount)
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