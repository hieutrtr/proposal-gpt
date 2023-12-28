import autogen
from prompts.plan_proposal import proposal_prompt
from functions.draft_proposal import store_draft_proposal
from custom_agents.dalle import DALLEAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from functions.draft_proposal import store_final_proposal

admin_retrieval_agent = {
    "name": "admin",
    "type": RetrieveUserProxyAgent,
    "system_message": """Assistant who has the content of draft proposal and list image url.""",
    "human_input_mode": "NEVER",
    "max_consecutive_auto_reply": 1,
}

proposal_finalizer_agent = {
    "name": "proposal_finalizer",
    "type": autogen.AssistantAgent,
    "system_message": """Act as a professional business development specialist in AI-powered software company.
Your goal is creating a compelling proposal slide deck for our client.
You will be provided draft proposal and list image and slide. 
Please ensure that each of these elements is presented in the proposal slides. Your goal is to create a persuasive and informative proposal that resonates with the client's needs and convinces them of the value we can provide.
Finally, store the draft of proposal in text format.
    """,
    "function_map": {
        "store_final_proposal": store_final_proposal,
    }
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