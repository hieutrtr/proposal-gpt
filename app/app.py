from proposal.configs import *
from proposal.agents import *
from proposal.group_chat import createProposalGroupChat
if __name__ == "__main__":
    proposal_agents = createProposalAgents(agents=[admin, proposal_writer, proposal_critic], configs=[])
    proposal_group_chat = createProposalGroupChat(agents=proposal_agents, config=config)
    # proposal_group_chat.set_human_mq(url)
    # proposal_group_chat.start_chat(stream_chatlog=True)
    proposal_group_chat.start_chat()