import unittest
from src import algorithms


class TestStringSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.text = "ababcabcabababd"
        self.pattern = "ababd"
        self.not_found_pattern = "xyz"

    def test_naive_search_found(self):
        self.assertEqual(algorithms.algorithms.naive_search(self.text, self.pattern), [10])

    def test_naive_search_not_found(self):
        self.assertEqual(algorithms.algorithms.naive_search(self.text, self.not_found_pattern), [])

    def test_naive_search_multiple_matches(self):
        self.assertEqual(algorithms.algorithms.naive_search("aaaaa", "aa"), [0, 1, 2, 3])

    def test_naive_search_empty_pattern(self):
        self.assertEqual(algorithms.algorithms.naive_search(self.text, ""), list(range(len(self.text) + 1)))

    def test_naive_search_empty_text(self):
        self.assertEqual(algorithms.naive_search("", self.pattern), [])

    def test_kmp_search_found(self):
        self.assertEqual(algorithms.kmp_search(self.text, self.pattern), [10])

    def test_kmp_search_not_found(self):
        self.assertEqual(algorithms.kmp_search(self.text, self.not_found_pattern), [])

    def test_kmp_search_multiple_matches(self):
        self.assertEqual(algorithms.kmp_search("aaaaa", "aa"), [0, 1, 2, 3])

    def test_kmp_search_empty_pattern(self):
        self.assertEqual(algorithms.kmp_search(self.text, ""), list(range(len(self.text) + 1)))

    def test_kmp_search_empty_text(self):
        self.assertEqual(algorithms.kmp_search("", self.pattern), [])

    def test_boyer_moore_search_found(self):
        self.assertEqual(algorithms.boyer_moore_search(self.text, self.pattern), [10])

    def test_boyer_moore_search_not_found(self):
        self.assertEqual(algorithms.boyer_moore_search(self.text, self.not_found_pattern), [])

    def test_boyer_moore_search_multiple_matches(self):
        self.assertEqual(algorithms.boyer_moore_search("aaaaa", "aa"), [0, 1, 2, 3])

    def test_boyer_moore_search_empty_pattern(self):
        self.assertEqual(algorithms.boyer_moore_search(self.text, ""), list(range(len(self.text) + 1)))

    def test_boyer_moore_search_empty_text(self):
        self.assertEqual(algorithms.boyer_moore_search("", self.pattern), [])

    def test_rabin_karp_found(self):
        self.assertEqual(algorithms.rabin_karp(self.text, self.pattern), [10])

    def test_rabin_karp_not_found(self):
        self.assertEqual(algorithms.rabin_karp(self.text, self.not_found_pattern), [])

    def test_rabin_karp_multiple_matches(self):
        self.assertEqual(algorithms.rabin_karp("aaaaa", "aa"), [0, 1, 2, 3])

    def test_rabin_karp_empty_pattern(self):
        self.assertEqual(algorithms.rabin_karp(self.text, ""), list(range(len(self.text) + 1)))

    def test_rabin_karp_empty_text(self):
        self.assertEqual(algorithms.rabin_karp("", self.pattern), [])


if __name__ == "__main__":
    unittest.main()
