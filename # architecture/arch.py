# architecture/arch.py

from agents.upstream_agent import UpstreamAgent
from agents.low_level_agent import LowLevelAgent
from agents.blended_low_level_agent import BlendedLowLevelAgent
from agents.task_tree import TaskTree

class ARCH:
    def __init__(self):
        self.upstream_agent = UpstreamAgent()
        self.task_tree = TaskTree()
        self.low_level_agents = []
        self.blended_agents = []

    def process_user_inquiry(self, user_inquiry):
        # Step 1: Analyze the user inquiry
        subtopics = self.upstream_agent.analyze_topic(user_inquiry)
        
        # Step 2: Delegate tasks to Low-Level Agents (LLAs)
        self.upstream_agent.delegate_tasks(subtopics)
        
        # Create LLAs for each subtopic
        for subtopic in subtopics:
            lla = LowLevelAgent(subtopic)
            self.low_level_agents.append(lla)
        
        # Step 3: Research phase for each LLA
        results = {}
        for lla in self.low_level_agents:
            results[lla.subtopic] = lla.conduct_research()
        
        # Step 4: Synthesize the information
        synthesized_data = self.upstream_agent.synthesize_information()
        return synthesized_data, results

    def create_blended_agent(self, ll_as):
        # Create a new Blended Low-Level Agent (BLLA) from a list of LLAs
        blla = BlendedLowLevelAgent(ll_as)
        self.blended_agents.append(blla)
        return blla
