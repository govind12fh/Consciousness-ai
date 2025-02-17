import unittest
from src.vedic_ai import VedicAI

class TestVedicAI(unittest.TestCase):
    def setUp(self):
        self.ai = VedicAI()

    def test_dharma_rule(self):
        self.assertIn("Dharma", self.ai.process_input("Should I harm others?"))

if __name__ == "__main__":
    unittest.main()

tests/test_vedic_ai.py
