import unittest

from utilities import dict_check


class TestExceptions(unittest.TestCase):

    def setUp(self):
        pass

    # pass if raise exception
    def test_raise_dict_check(self):
        func_name = 'test_function'
        var = ()
        self.assertRaises(TypeError, dict_check, func_name, var)
        var = []
        self.assertRaises(TypeError, dict_check, func_name, var)
        var = ()
        self.assertRaises(TypeError, dict_check, func_name, var)


if __name__ == '__main__':
    unittest.main()
