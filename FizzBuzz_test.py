import unittest
import FizzBuzz as FizzBuzzClass

class FizzBuzzTest(unittest.TestCase):
    main = FizzBuzzClass.FizzBuzz()  # instantiate the Person Class

    # test case function to check the Person.set_name function
    def test_shall_pass(self):
        self.assertTrue(self.main.handle())
