import unittest

from pre_processing import percentage, process_conditions
from utilities import dict_check
import pandas as pd


class TestExceptions(unittest.TestCase):

    def setUp(self):
        dataset_address = 'C:\\Users\\rtesta\\Documents\\z -Personal\\ML_drug_test\\drugsComTest_raw.csv'
        self.dataset = pd.read_csv(dataset_address)

    # Must raise the TypeError exception
    # if the variable "var" passed to the
    # function dict_check is not a dictionary
    def test_raise_dict_check(self):
        func_name = 'test_function'
        var = ()
        self.assertRaises(TypeError, dict_check, func_name, var)
        var = []
        self.assertRaises(TypeError, dict_check, func_name, var)
        var = ()
        self.assertRaises(TypeError, dict_check, func_name, var)

    # percentage test
    def test_percentage(self):
        self.assertEquals(list(percentage(process_conditions(self.dataset).values()).sum()), 100)


if __name__ == '__main__':
    unittest.main()
