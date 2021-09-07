def should_drink_coffee(is_sleepy = False):
    if(is_sleepy):
        return 'Drink Coffee!'
    else:
        return 'Continue what you are doing...'

import unittest

class TestMain(unittest.TestCase):
    # Executed before each test function
    def setUp(self):
        # TODO
        # Maybe connect to the database?
        pass

    # Executed after each test function
    def tearDown(self):
        # TODO
        # Maybe close database connection?
        pass

    # Unit test to cover the 'True' path from 'should_drink_coffee'
    def test_should_drink_coffee_sleepy(self):
        is_sleepy = True
        expected = 'Drink Coffee!'
        actual = should_drink_coffee(is_sleepy)
        self.assertEqual(actual, expected)

    # Unit test to cover the 'False' path from 'should_drink_coffee'
    def test_should_drink_coffee_not_sleepy(self):
        is_sleepy = False
        expected = 'Continue what you are doing...'
        actual = should_drink_coffee(is_sleepy)
        self.assertEqual(actual, expected)

unittest.main()