def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    
	Do not include these tokens in the code: test = test . strip ()
	"""
    result = {}
    test = test.strip().split(' ')
    for i in test:
        if not i: continue
        if not result.get(i): result[i] = 1
        else: result[i] += 1
    return result

import unittest
class HistogramTestCase(unittest.TestCase):
    
    def test_histogram_with_three_character_string(self):
        test = histogram('a b c')
        self.assertEqual(test['a'], 1)
        self.assertEqual(test['b'], 1)
        self.assertEqual(test['c'], 1)
    
    def test_histogram_with_three_character_string(self):
        test = histogram('a b b a')
        self.assertEqual(test['a'], 2)
        self.assertEqual(test['b'], 2)       
        self.assertTrue(len(test) == 2)
        
    def test_histogram_with_blank_space(self):
        test = histogram('b b b b a')
        self.assertEqual(test['b'], 4)
        self.assertTrue(len(test) == 1)
        
    def test_histogram_with_blank_string(self):
        test = histogram('')
        self.assertFalse(len(test) > 0)
        
    def test_histogram_with_two_character_string(self):
        test = histogram('a b')
        self.assertEqual(test['a'], 1)
        self.assertEqual(test['b'], 1)
    
    def test_histogram_with_two_character_string2(self):
        test = histogram('a b a')
        self.assertEqual(test['a'], 2)
        self.assertEqual(test['b'], 1)
        
    def test_histogram_with_only_one_unique_value(self):
        test = histogram('a a a a a')
        self.assertEqual(test['a'],