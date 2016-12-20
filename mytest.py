import unittest

import pysimplib_LD.mymath as mymod

class SimplisticTest(unittest.TestCase):

    def test_add(self):
    	x = mymod.myadd(10,20)
        self.assertEqual(x, 30)

    def test_sub(self):
    	x = mymod.mysub(10,20)
    	self.assertEqual(x, -10)

if __name__ == '__main__':
    unittest.main()