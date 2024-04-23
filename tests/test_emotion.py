# tests/test_emotion.py

import unittest
from app.emotion import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test_emotion_predictor(self):
        response = emotion_predictor("I am very happy")
        self.assertIn('emotions', response)

if __name__ == '__main__':
    unittest.main()
