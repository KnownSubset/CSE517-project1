__author__ = 'nathan'

import unittest
import discretize_data

class MyTestCase(unittest.TestCase):
    def test_on_file(self):
        results = discretize_data.discrete("/Users/nathan/Development/CSE517/project1/data.txt", "/Users/nathan/Development/CSE517/project1/nans as mean")
        self.assertEqual(results, [["01","11","21","31"],["02","12","22","32"],["03","13","23","33"],["04","14","24","34"]])
    def test_discretize_a_row(self):
        results = discretize_data.discretize_row({'col1':5,'col2':10.1, 'col3':15},[ 7, 4, 11, 10], 'col2')
        self.assertEqual(results, ['True','True','False','True'])
    def test_discretize_a_row_that_contains_nans(self):
        results = discretize_data.discretize_row({'col1':5,'col2':10.1, 'col3':15},[ 'nan', 7, 4, 11, 10, 20, 'nan'], 'col2')
        self.assertEqual(results, ['False','True','True','False','True','False','False'])


if __name__ == '__main__':
    unittest.main()