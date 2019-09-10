from unittest import TestCase
import unittest

def biggest_loss(prices):
    if type(prices) != list:
        return -1
    if(len(prices))<1:
        return -2
    #worst loss (wl)
    wl = 0
    lenlist = len(prices)
    iterprices = iter(prices)
    previous = next(iterprices)
    for pricevl in iterprices:
        cwl=pricevl - previous
        if(cwl<0):
            if -cwl>wl:
                wl=-cwl
        previous=pricevl
    return wl

class TestBiggestLoss(TestCase):
    def test_biggest_loss(self):
        d = 1 #not a list
        dd = biggest_loss(d)
        self.assertEqual(dd, -1)
        d = [] #empty list
        dd = biggest_loss(d)
        self.assertEqual(dd, -2)
        d = [7] #one element list
        dd = biggest_loss(d)
        self.assertEqual(dd, 0)
        d = [0,1,5,13,18] # always crescent list of prices
        dd = biggest_loss(d)
        self.assertEqual(dd, 0)
        d = [121,116,83,41,27,16,1] # always decrescent list of prices
        dd = biggest_loss(d)
        self.assertEqual(dd, 42)
        d = [1, 3, 17, 12, 11, 24, 3, 28, 12] # crescent and decrescent list of prices
        dd = biggest_loss(d)
        self.assertEqual(dd, 21)
        ## tests for lists with elements that are not floats could have been done.
        ## However, the verification in the function implemented to avoid
        ## exceeding the exercise time

unittest.main()
