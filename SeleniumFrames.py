import unittest


class Employee(unittest.TestCase):

    def test_tc1(self):
        print("test1")
        raise ZeroDivisionError
        print("a")

    def test_tc2(self):
        print("test2")
        print("b")
