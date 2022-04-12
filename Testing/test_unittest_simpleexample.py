from simple_calc import SimpleCalc

import unittest

class Calctests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
