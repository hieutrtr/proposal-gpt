from autogen import GroupChat, GroupChatManager, Agent, AssistantAgent
import random
manager = None
ORG_PROMPT = "This organization chat is about {}. Please work together to solve the problem."
ORG_PROCESS = """There are {} teams in this organization. The teams are 
{}
--- Working process:
Each team leader is responsible for ensuring their team's deliverables are completed on time and meet the required standards.
After each phase, team leaders will coordinate with the next team's leader to ensure smooth handover and clarify any queries.
Regular cross-team meetings should be scheduled for updates, addressing challenges, and ensuring alignment with the project goals.
"""
TEAM_PROMPT = """{} team:
* Task: {}
* Deliverable: {}
* Communication: {}
"""

class CustomGroupChat(GroupChat):
    def __init__(self, agents, messages, max_round=10):
        super().__init__(agents, messages, max_round)
        self.previous_speaker = None  # Keep track of the previous speaker
    
    def select_speaker(self, last_speaker: Agent, selector: AssistantAgent):
        # Check if last message suggests a next speaker or termination
        last_message = self.messages[-1] if self.messages else None
        if last_message:
            if 'NEXT:' in last_message['content']:
                suggested_next = last_message['content'].split('NEXT: ')[-1].strip()
                print(f'Extracted suggested_next = {suggested_next}')
                try:
                    return self.agent_by_name(suggested_next)
                except ValueError:
                    pass  # If agent name is not valid, continue with normal selection
            elif 'TERMINATE' in last_message['content']:
                try:
                    return self.agent_by_name('User_proxy')
                except ValueError:
                    pass  # If 'User_proxy' is not a valid name, continue with normal selection
        
        team_leader_names = [agent.name for agent in self.agents if agent.name.endswith('1')]

        if last_speaker.name in team_leader_names:
            team_letter = last_speaker.name[0]
            possible_next_speakers = [
                agent for agent in self.agents if (agent.name.startswith(team_letter) or agent.name in team_leader_names) 
                and agent != last_speaker and agent != self.previous_speaker
            ]
        else:
            team_letter = last_speaker.name[0]
            possible_next_speakers = [
                agent for agent in self.agents if agent.name.startswith(team_letter) 
                and agent != last_speaker and agent != self.previous_speaker
            ]

        self.previous_speaker = last_speaker

        if possible_next_speakers:
            next_speaker = random.choice(possible_next_speakers)
            return next_speaker
        else:
            return None

class ProposalOrgChart:
    def __init__(self, epic, teams=[], config={}):
        ## handle exceptions
        if epic is None:
            raise Exception("Epic should not be empty.")
        if len(teams) < 2:
            raise Exception("There should be at least 2 teams in a organization.")
        if not config:
            raise Exception("Config should not be empty.")
        self.teams = teams
        self.config = config
        self.epic = epic

    def startUp(self, input):
        self.agents = [agent for team in self.teams for agent in team["agents"]]
        init_agents = self.agents[0]
        team_definitions = ["\n".join([TEAM_PROMPT.format(team["name"], team["task"], team["deliverable"], team["communication"]) for team in self.teams])]
        groupchat = CustomGroupChat(agents=self.agents, messages=[
            # {"role": "system", "content": ORG_PROMPT.format(self.epic)},
            # {"role": "system", "content": ORG_PROCESS.format(len(self.teams), team_definitions)},
            ORG_PROMPT.format(self.epic),
            ORG_PROCESS.format(len(self.teams), team_definitions)
        ], max_round=50)
        self.manager = GroupChatManager(groupchat=groupchat, llm_config=self.config)
        init_agents.initiate_chat(
            self.manager,
            message=input,
        )