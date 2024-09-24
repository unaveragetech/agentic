# agents/upstream_agent.py

from agents.low_level_agent import LowLevelAgent
from architecture.arch import ARCH

class UpstreamAgent:
    def __init__(self):
        self.tasks = []
        self.status = {}  # Track status of each Low-Level Agent (LLA)
        self.arch = ARCH()  # Initialize the architecture manager

    def analyze_topic(self, topic, depth=1):
        """
        Analyze the provided topic to identify subtopics.
        
        Args:
            topic (str): The broad topic submitted by the user.
            depth (int): Depth of research to be conducted.

        Returns:
            list: A list of identified subtopics.
        """
        if not topic:
            raise ValueError("Topic cannot be empty.")
        print(f"Analyzing topic: '{topic}' with depth: {depth}")
        
        # Basic analysis to split the topic into subtopics
        subtopics = topic.split(" using ")  # Example: ["web development", "Python"]
        return subtopics, depth

    def delegate_tasks(self, subtopics, depth):
        """
        Delegate research tasks to Low-Level Agents based on the identified subtopics.
        
        Args:
            subtopics (list): A list of identified subtopics.
            depth (int): Depth of research for each subtopic.
        """
        self.tasks = []
        for subtopic in subtopics:
            lla = LowLevelAgent(subtopic, depth)  # Pass depth to each LLA
            self.tasks.append(lla)
            self.status[subtopic] = "Pending"  # Initial status
            self.arch.assign_task(lla)  # Notify ARCH about the new task

    def compile_results(self):
        """
        Compile research results from all Low-Level Agents.
        
        Returns:
            dict: A dictionary of subtopic results and their status.
        """
        results = {}
        for task in self.tasks:
            try:
                result = task.conduct_research()
                results[task.subtopic] = result
                self.status[task.subtopic] = "Completed" if result else "Failed"
            except Exception as e:
                results[task.subtopic] = f"Error: {str(e)}"
                self.status[task.subtopic] = "Error"
        return results

    def get_status(self):
        """
        Get the current status of all delegated tasks.
        
        Returns:
            dict: The status of each task.
        """
        return self.status

    def provide_summary(self, results):
        """
        Provide a summary of the research findings.
        
        Args:
            results (dict): Results from the research tasks.
        
        Returns:
            str: Summary of the results.
        """
        summary = "Research Summary:\n"
        for subtopic, result in results.items():
            summary += f"- {subtopic}: {result}\n"
        return summary.strip()
