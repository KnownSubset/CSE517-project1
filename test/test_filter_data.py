__author__ = 'nathan'

import unittest
import filter_data

class MyTestCase(unittest.TestCase):
    def test_on_file(self):
        filters = ["GI_4585642-S", "GI_23312375-A", "GI_5453687-S", "GI_21729887-A","GI_31442419-S", "GI_42659113-S","GI_44917603-S","GI_40538791-S", "GI_40254954-S","GI_27475984-S", "GI_37547175-S","GI_18677732-S",
                  "GI_20336751-I","GI_27436998-S","GI_34335274-A","GI_16936521-S", "GI_4557446-S", "GI_24308166-S","GI_16507207-S","GI_30240931-S","GI_13376557-S","GI_13899226-S","GI_27734844-S","GI_41327770-S","GI_37620162-I","GI_40254432-S","GI_16306581-S","GI_9624970-S",
                  "GI_40549398-S","GI_4502860-S", "GI_13787214-I","GI_40255112-S","GI_41281388-S","GI_13259542-A"]
        results = filter_data.filter_file("/Users/nathan/Development/CSE517/project1/data.txt", filters)
        self.assertEqual(results, [["01","11","21","31"],["02","12","22","32"],["03","13","23","33"],["04","14","24","34"]])
    def test_on_rows(self):
        filters = ["GI_4585642-S", "GI_23312375-A", "GI_5453687-S"]
        data = [["GI_4585642-S","1"], ["GI_23312375-A1","1"], ["GI_5453687-S","1"],["GI_4585642-S2","1"], ["GI_23312375-A","1"], ["GI_5453687-S3","1"]]
        results = filter_data.filter_data(data, filters)
        self.assertEqual(results, [["GI_4585642-S","1"], ["GI_5453687-S","1"], ["GI_23312375-A","1"]])
    def test_on_rows2(self):
        results = filter_data.filter_file_using_filtered_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as mean", 5)
        self.assertEqual(results, [["GI_4585642-S","1"], ["GI_5453687-S","1"], ["GI_23312375-A","1"]])
    def test_on_process_file(self):
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as mean", 2)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as mean", 4)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as mean", 8)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as mean", 16)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as mean", 32)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as mean", 64)
        self.assertEqual(results, [["GI_4585642-S","1"], ["GI_5453687-S","1"], ["GI_23312375-A","1"]])
    def test_on_process_file_as_zeros(self):
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as zero", 2)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as zero", 4)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as zero", 8)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as zero", 16)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as zero", 32)
        results = filter_data.process_file("/Users/nathan/Development/CSE517/project1/data.csv", "/Users/nathan/Development/CSE517/project1/nans as zero", 64)
        self.assertEqual(results, [["GI_4585642-S","1"], ["GI_5453687-S","1"], ["GI_23312375-A","1"]])


if __name__ == '__main__':
    unittest.main()
  