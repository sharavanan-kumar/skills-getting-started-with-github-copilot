import unittest
import numpy as np
from python_gha_demo.correlation import calculate_correlation

class TestCorrelation(unittest.TestCase):

    def test_correlation_positive(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        expected_correlation = 0.858186
        self.assertAlmostEqual(calculate_correlation(x, y), expected_correlation, places=5)

    def test_correlation_negative(self):
        x = [1, 2, 3, 4, 5]
        y = [5, 4, 3, 2, 1]
        expected_correlation = -1.0
        self.assertAlmostEqual(calculate_correlation(x, y), expected_correlation, places=5)

    def test_correlation_zero(self):
        x = [1, 2, 3, 4, 5]
        y = [5, 1, 4, 2, 3]
        expected_correlation = -0.273200
        self.assertAlmostEqual(calculate_correlation(x, y), expected_correlation, places=5)

    def test_correlation_same_values(self):
        x = [1, 1, 1, 1, 1]
        y = [1, 1, 1, 1, 1]
        expected_correlation = np.nan
        self.assertTrue(np.isnan(calculate_correlation(x, y)))
