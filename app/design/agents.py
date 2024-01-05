import autogen
from prompts.plan_proposal import proposal_prompt
from functions.draft_proposal import store_draft_proposal
from custom_agents.dalle import DALLEAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

retrieval_admin_agent = {
    "name": "admin",
    "type": RetrieveUserProxyAgent,
    "system_message": """Assistant who has the content of draft proposal.""",
    "human_input_mode": "NEVER",
    "max_consecutive_auto_reply": 3,
}

visualizer_agent = {
    "name": "visualizer",
    "type": autogen.AssistantAgent,
    "system_message": """Visualizer. Read through the proposal and provide prompts for pictures generation based on content in every section of the proposal.
    The response must be in array of json format, each json object contains the slide_title and image_prompt.
    """,
}

designer_agent = {
    "name": "designer",
    "type": DALLEAgent,
    "system_message": "Designer. Read through the list of slide_title and prompt pairs. Generate an image based on each of slide_titlte and prompt pairs",
}



def createProposalAgents(agents=[], configs=[]):
    proposal_agents = []
    for i, define in enumerate(agents):
        # check if define["type"] is class RetrieveUserProxyAgent
        agent = None
        if define["type"] == RetrieveUserProxyAgent:
            agent = define["type"](
                name=define["name"],
                system_message=define["system_message"],
                human_input_mode=define["human_input_mode"],
                max_consecutive_auto_reply=define["max_consecutive_auto_reply"],
                retrieve_config=configs[i],
            )
        else:
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