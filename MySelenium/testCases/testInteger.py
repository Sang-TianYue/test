
# coding:utf-8

import unittest

class testInteger(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(1+2, 3)
        print("testAdd passed")

    def testMultiply(self):
        self.assertEqual( 0*10, 0)
        print("testMuitiply passed")

if __name__ == "__main__":
    unittest.main(verbosity=2)
