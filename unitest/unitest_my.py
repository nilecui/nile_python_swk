#!/usr/bin/python
#-*- coding:utf-8 -*-

import random
import unittest

class TestSquenceFunction(unittest.TestCase):
    def setUp(self):
        print "setup-->\n"
        self.seq=range(10)

    def test_shuffle(self):
        #make sure the shuffle sequence does not lose any elements
        print "--test_shffle--"
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq,range(10))

        #should raise an exception for an immutable sequence
        self.assertRaises(TypeError,random.shuffle, (1,2,3))

    def test_choice(self):
        print "--test_choice--"
        elements=random.choice(self.seq)
        self.assertTrue(elements in self.seq)

    def test_sample(self):
        print "--test_sample--"
        with self.assertRaises(ValueError):
            random.sample(self.seq,20)
        for element in random.sample(self.seq,5):
            self.assertTrue(element in self.seq)

if __name__=='__main__':
    #unittest.main()
    suite=unittest.TestLoader().loadTestsFromTestCase(TestSquenceFunction)
    unittest.TextTestRunner(verbosity=2).run(suite)
