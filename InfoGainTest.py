import InformationGain

__author__ = 'nathan'

import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(InformationGain.discretize([3,9 ,2 ,1]), {1.5:1,2.5:2,6.0:3})
    def test_classificationRanges(self):
        positive = [1.0,3,5]
        negative = [4,6,8]
        expected = {2: {'p':1,'n': 0}, 3.5: {'p':2,'n': 0}, 4.5: {'p':2,'n': 1}, 5.5: {'p':3,'n': 1}, 7.0: {'p':3,'n': 2}}
        self.assertEqual(InformationGain.classification({'p':positive, 'n':negative}), expected)
#    def test_entropy(self):
#        positive = [1.0,3,5]
#        negative = [4,6,8]
#        expected = {2: {'<':0, '>': 0},3.5: {'<':2,'>': 0}, 4.5: {'<':2,'>': 1}, 5.5: {'<':3,'>': 1}, 7.0: {'<':3,'>': 2}}
#        self.assertEqual(InformationGain.entropyIn({'p':positive, 'n':negative}), expected)
#    def test_entropy(self):
#        self.maxDiff = None
#        positive = [95, 85, 90]
#        negative = [125, 100, 70, 120, 60, 220, 75]
#        expected = {65.0: {'>':0.826466251, '<': 0},
#                    72.5: {'>':0.763547202,'<': 0},
#                    80.0: {'>':0.689659695,'<': 0},
#                    87.5: {'>':0.5509775,'<': 0.32451125},
#                    92.5: {'>':0.360964047,'<': 0.485475297},
#                    97.5: {'>':0,'<': 0.6},
#                    110.0: {'>':0,'<': 0.689659695},
#                    122.5: {'>':0,'<': 0.763547202},
#                    172.5: {'>':0,'<': 0.826466251}}
#        results = InformationGain.entropyIn({'no': negative, 'yes': positive})
#        self.assertEqual(results, expected)
    def test_infoGain(self):
        self.maxDiff = None
        positive = [95, 85, 90]
        negative = [125, 100, 70, 120, 60, 220, 75]
        expected = {65.0: 0.054824649,
                    72.5: 0.117743697,
                    80.0: 0.191631204,
                    87.5: 0.005802149,
                    92.5: 0.034851555,
                    97.5: 0.281290899,
                    110.0: 0.191631204,
                    122.5: 0.117743697,
                    172.5: 0.054824649}
        results = InformationGain.informationGain({'no': negative, 'yes': positive})
        self.assertEqual(results, expected)

if __name__ == '__main__':
    unittest.main()
