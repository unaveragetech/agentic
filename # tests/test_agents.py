# tests/test_agents.py

import unittest
from agents.upstream_agent import UpstreamAgent
from agents.low_level_agent import LowLevelAgent
from agents.blended_low_level_agent import BlendedLowLevelAgent

class TestAgents(unittest.TestCase):

    def test_upstream_agent(self):
        ua = UpstreamAgent()
        subtopics = ua.analyze_topic("web development using Python")
        self.assertEqual(len(subtopics), 3)  # Assuming the mock returns three subtopics

        ua.delegate_tasks(subtopics)
        self.assertEqual(ua.tasks, subtopics)  # Check if tasks are delegated correctly

    def test_low_level_agent(self):
        lla = LowLevelAgent("Django")
        research_data = lla.conduct_research()
        self.assertIn("data", research_data)  # Check if data key exists

    def test_blended_low_level_agent(self):
        lla1 = LowLevelAgent("Flask")
        lla2 = LowLevelAgent("CSS")
        blla = BlendedLowLevelAgent([lla1, lla2])
        consolidated_data = blla.consolidate_information()
        self.assertIn("Flask", consolidated_data)
        self.assertIn("CSS", consolidated_data)

if __name__ == '__main__':
    unittest.main()
