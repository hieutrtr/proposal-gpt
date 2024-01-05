import autogen
from prompts.plan_proposal import proposal_prompt
from functions.draft_proposal import store_draft_proposal

proposal_admin_agent = {
    "name": "admin",
    "type": autogen.UserProxyAgent,
    "system_message": """A human admin. Interact with the proposal_writer and proposal_critic to draft the proposal, proposal_critic will verify and give comments to improve the draft proposal content and structure. 
    The draft of proposal needs to be approved by this admin.
    """,
}

proposal_writer_agent = {
    "name": "proposal_writer",
    "type": autogen.AssistantAgent,
    "system_message": proposal_prompt,
    "function_map": {
                "store_draft_proposal": store_draft_proposal,
            }
}

proposal_critic_agent = {
    "name": "proposal_critic",
    "type": autogen.AssistantAgent,
    "system_message": "Critic. Double check the proposal from the executer and provide feedback.",
}



def createProposalAgents(agents=[], configs=[]):
    proposal_agents = []
    for i, define in enumerate(agents):
        agent = define["type"](
            name=define["name"],
            system_message=define["system_message"],
            llm_config=configs[i],
        )
        agent.register_function(
            function_map=define.get("function_map", {}),
        )
        proposal_agents.append(agent)
    return proposal_agents