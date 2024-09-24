# tests/test_architecture.py

import unittest
from architecture.arch import ARCH

class TestARCH(unittest.TestCase):

    def test_process_user_inquiry(self):
        arch = ARCH()
        synthesized_data, results = arch.process_user_inquiry("web development using Python")

        # Check if synthesized data is returned
        self.assertIn("summary", synthesized_data)
        
        # Check if results contain expected subtopics
        self.assertIn("subtopic1", results)
        self.assertIn("subtopic2", results)
        self.assertIn("subtopic3", results)

    def test_create_blended_agent(self):
        arch = ARCH()
        lla1 = LowLevelAgent("Flask")
        lla2 = LowLevelAgent("Django")
        blla = arch.create_blended_agent([lla1, lla2])
        self.assertIsInstance(blla, BlendedLowLevelAgent)  # Check if a BLLA is created

if __name__ == '__main__':
    unittest.main()
