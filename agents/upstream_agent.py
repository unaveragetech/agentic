# agents/upstream_agent.py

from agents.low_level_agent import LowLevelAgent
from architecture.arch import ARCH

class UpstreamAgent:
    def __init__(self):
        self.tasks = []
        self.status = {}  # Track status of each LLA

    def analyze_topic(self, topic):
        if not topic:
            raise ValueError("Topic cannot be empty.")
        print(f"Analyzing topic: {topic}")
        subtopics = topic.split(" using ")  # Example: ["web development", "Python"]
        return subtopics

    def delegate_tasks(self, subtopics):
        self.tasks = []
        for subtopic in subtopics:
            lla = LowLevelAgent(subtopic)
            self.tasks.append(lla)
            self.status[subtopic] = "Pending"  # Initial status

    def compile_results(self):
        results = {}
        for task in self.tasks:
            result = task.conduct_research()
            results[task.subtopic] = result
            self.status[task.subtopic] = "Completed" if result else "Failed"
        return results

    def get_status(self):
        return self.status
