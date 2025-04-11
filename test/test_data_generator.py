import unittest
import numpy as np
import string
from unittest.mock import patch


# Simulación de constants
class constants:
    MIN_LENGTH_PATTERN = 3
    MAX_LENGTH_PATTERN = 6


# Importar aquí la función si está en otro archivo
from src.data_generator import generate_random_text_and_pattern


class TestGenerateRandomTextAndPattern(unittest.TestCase):
    def test_text_length_is_correct(self):
        text_length = 100
        pattern_probability = 0.5
        text, pattern = generate_random_text_and_pattern(text_length, pattern_probability)
        self.assertEqual(len(text), text_length)

    def test_pattern_is_uppercase_and_valid_length(self):
        text_length = 50
        pattern_probability = 0.5
        text, pattern = generate_random_text_and_pattern(text_length, pattern_probability)
        self.assertTrue(all(c in string.ascii_uppercase for c in pattern))
        self.assertGreaterEqual(len(pattern), constants.MIN_LENGTH_PATTERN)
        self.assertLessEqual(len(pattern), constants.MAX_LENGTH_PATTERN)

    def test_pattern_never_longer_than_text(self):
        text_length = 5  # menor que MAX_LENGTH_PATTERN
        pattern_probability = 1.0
        text, pattern = generate_random_text_and_pattern(text_length, pattern_probability)
        self.assertLessEqual(len(pattern), text_length)

    @patch("numpy.random.random")
    def test_insert_variation_of_pattern(self, mock_random):
        # Fuerza que siempre se intente insertar una variación del patrón
        mock_random.return_value = 0.1
        text, pattern = generate_random_text_and_pattern(50, 1.0)
        self.assertTrue(any(pattern not in text[i : i + len(pattern)] for i in range(len(text) - len(pattern))))

    def test_low_probability_minimizes_pattern_insertions(self):
        text, pattern = generate_random_text_and_pattern(100, 0.0)
        self.assertTrue(pattern not in text)


if __name__ == "__main__":
    unittest.main()
