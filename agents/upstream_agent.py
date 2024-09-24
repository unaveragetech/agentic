# agents/upstream_agent.py

from agents.low_level_agent import LowLevelAgent
from architecture.arch import ARCH

class UpstreamAgent:
    def __init__(self):
        self.tasks = []

    def analyze_topic(self, topic):
        # Simple mock analysis: split topic into subtopics
        subtopics = topic.split(" using ")  # Example: ["web development", "Python"]
        return subtopics

    def delegate_tasks(self, subtopics):
        self.tasks = []
        for subtopic in subtopics:
            lla = LowLevelAgent(subtopic)
            self.tasks.append(lla)

    def compile_results(self):
        # Compile results from all tasks
        results = [task.conduct_research() for task in self.tasks]
        return results
