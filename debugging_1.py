from unittest import TestCase
import unittest

def increment_dictionary_values(d, i):
    dd = {}
    for k,v in d.items():
        dd[k] = v+i
    return dd

class TestIncrementDictionaryValues(TestCase):
    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)

unittest.main()
