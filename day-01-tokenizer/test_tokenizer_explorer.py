import unittest

from tokenizer_explorer import tokenize, detokenize


class TestTokenizerExplorer(unittest.TestCase):

    def test_basic_tokenization(self):
        result = tokenize("Hello World!")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_round_trip(self):
        original = "I am learning AI Engineering."
        result = detokenize(tokenize(original))

        self.assertEqual(original, result)

    def test_empty_string(self):
        result = tokenize("")
        self.assertEqual(result, [])

    def test_unicode_text(self):
        original = "Hello پاکستان"
        result = detokenize(tokenize(original))

        self.assertEqual(original, result)

    def test_deterministic_tokenization(self):
        text = "Artificial Intelligence"

        self.assertEqual(tokenize(text), tokenize(text))


if __name__ == "__main__":
    unittest.main()