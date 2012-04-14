__author__ = 'nathan'

import unittest
import tranpose_csv

class MyTestCase(unittest.TestCase):
    def test_something(self):
        results = tranpose_csv.transpose([["1","2","5"],["3","4", "6"]])
        self.assertEqual(results, [["1","3"],["2","4"], ["5", "6"]])
    def test_larger(self):
        results = tranpose_csv.transpose([["01","02","03","04"],["11","12","13","14"],["21","22","23","24"],["31","32","33","34"]])
        self.assertEqual(results, [["01","11","21","31"],["02","12","22","32"],["03","13","23","33"],["04","14","24","34"]])
    def test_on_file(self):
        results = tranpose_csv.transpose_file("/Users/nathan/Development/CSE517/project1/discrete_zero_value.csv")
        self.assertEqual(results, [["01","11","21","31"],["02","12","22","32"],["03","13","23","33"],["04","14","24","34"]])
    def test_on_file2(self):
        results = tranpose_csv.transpose_tsv_file("/Users/nathan/Development/CSE517/project1/test.tsv")
        self.assertEqual(results, [["01","11","21","31"],["02","12","22","32"],["03","13","23","33"],["04","14","24","34"]])


if __name__ == '__main__':
    unittest.main()
