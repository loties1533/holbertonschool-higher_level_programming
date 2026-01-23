#!/usr/bin/python3
"""unittest pour la fonction max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_liste_vide(self):
        self.assertIsNone(max_integer([]))
    
    def test_un_element(self):
        self.assertEqual(max_integer([6]), 6)

    def test_liste_croissante(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_liste_desordre(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_negatifs(self):
        self.assertEqual(max_integer([-6, -5, -3]), -3)
    
    def test_max_debut(self):
        self.assertEqual(max_integer([15, 3, 6, 1]), 15)

    def test_max_fin(self):
        self.assertEqual(max_integer([6, 3, 1, 15]), 15)

    def test_max_milieu(self):
        self.assertEqual(max_integer([1, 10, 2, 3]), 10)
     
    def test_float(self):
        self.assertEqual(max_integer([5.5, 9.7, 0.2]), 9.7)

    def test_doublon(self):
        self.assertEqual(max_integer([6, 6, 6]), 6)

if __name__ == '__main__':
    unittest.main()