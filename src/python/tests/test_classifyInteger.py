import os
import unittest
import project.classifyInteger as classifyInteger

class ClassifyIntegerTest(unittest.TestCase):

    def test_get_integer(self):
        """Test that image is correctly classified."""
        result = classifyInteger.get_integer(os.path.join(os.path.dirname(
                        os.path.abspath(__file__)), "data/test_three_blue.png"))
        self.assertEqual(result, 3)
