import InformationGain

__author__ = 'nathan'

import unittest

class MyTestCase(unittest.TestCase):
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
