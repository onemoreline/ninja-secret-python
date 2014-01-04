'''
Created on 4 Oca 2014

@author: YY000001
'''
import unittest


class Test(unittest.TestCase):


    def testTester(self):
        pass
    def testTester2(self):
        #pass
        assert 1<2, "fail?"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTester']
    unittest.main()