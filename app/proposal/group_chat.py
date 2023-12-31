from autogen import GroupChat, GroupChatManager

manager = None
GROUP_PROMPT = "This group chat is about {}. Please work together to solve the problem."

class ProposalGroupChat:
    def __init__(self, agents=[], config={}):
        ## handle exceptions
        if len(agents) < 2:
            raise Exception("There should be at least 2 agents in a group chat.")
        if not config:
            raise Exception("Config should not be empty.")
        self.agents = agents
        self.config=config

    def startGroupChat(self, input):
        init_agents = self.agents[0]
        groupchat = GroupChat(agents=self.agents, messages=[GROUP_PROMPT.format(self.feature)], max_round=50)
        self.manager = GroupChatManager(groupchat=groupchat, llm_config=self.config)
        init_agents.initiate_chat(
            self.manager,
            message=input,
        )

    def formTeam(self, name, feature, deliverable, communication):
        team = {
            "agents": self.agents,
            "name": name,
            "task": feature,
            "deliverable": deliverable,
            "communication": communication
        }
        return team