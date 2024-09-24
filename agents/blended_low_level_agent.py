# agents/blended_low_level_agent.py

class BlendedLowLevelAgent:
    def __init__(self, agents):
        self.agents = agents

    def consolidate_information(self):
        consolidated_data = {}
        for agent in self.agents:
            data = agent.conduct_research()
            if data:
                consolidated_data[agent.subtopic] = data
        return consolidated_data

    def get_agent_status(self):
        return {agent.subtopic: agent.status for agent in self.agents}
