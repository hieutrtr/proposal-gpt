import autogen

admin = {
    "name": "admin",
    "system_message": """A human admin. Interact with the proposal_writer and proposal_critic to draft the proposal, proposal_critic will verify and give comments to improve the draft proposal content and structure. 
    The draft of proposal needs to be approved by this admin.
    """,
    "code_execution_config": False,
}

proposal_writer = {
    "name": "proposal_writer",
    "system_message": "Proposal writer. Write the proposal.",
}

proposal_critic = {
    "name": "proposal_critic",
    "system_message": "Critic. Double check the proposal from the executer and provide feedback.",
}

def createProposalAgents(agents=[], configs=[]):
    proposal_agents = []
    for i, agent in enumerate(agents):
        proposal_agents.append(autogen.AssistantAgent(
            name=agent["name"],
            system_message=agent["system_message"],
            code_execution_config=agent["code_execution_config"],
            llm_config=configs[i],
        ))
    return proposal_agents