from proposal.configs import *
from proposal.agents import *
from proposal.group_chat import ProposalGroupChat

input = """
<client_domain> (Client Domain): Healthcare

<client_problems_list> (Client Problems List):

Inefficient patient data management and retrieval.
High administrative workload for healthcare professionals.
Difficulty in early disease detection and diagnosis.
Limited access to real-time patient insights.
Privacy and security concerns related to patient data.
<solution> (Solution):

Proposed Solution Structure:
Component 1: Implement an AI-driven Electronic Health Record (EHR) system for efficient data management and retrieval.
Component 2: Develop a virtual assistant to automate administrative tasks and streamline workflows for healthcare professionals.
Component 3: Create a predictive analytics module for early disease detection and diagnosis.
Component 4: Build a secure patient portal for real-time access to medical records and insights.

<case_studies_list> (Case Studies List):

Case Study 1: Enhanced Patient Care

Description: Demonstrates how our AI-powered EHR system improved patient care and reduced errors in a hospital, resulting in a 20% reduction in readmissions.
Metrics: Reduced readmissions, improved patient outcomes, healthcare provider testimonial.
Case Study 2: Administrative Efficiency

Description: Highlights how our virtual assistant reduced administrative workload for a medical practice, leading to a 30% increase in appointment scheduling efficiency.
Metrics: Administrative time savings, appointment scheduling accuracy, client testimonial.
Case Study 3: Disease Detection

Description: Illustrates our success in early disease detection using predictive analytics, resulting in a 40% increase in early-stage diagnoses for a healthcare institution.
Metrics: Early-stage diagnoses, patient outcomes, healthcare provider feedback.

<success_stories_list> (Success Stories List):

Success Story 1: Revenue Growth

Description: Our AI-powered solutions contributed to a 15% increase in revenue for a healthcare client by improving patient care and operational efficiency.
Metrics: Revenue growth, ROI, client testimonial.
Success Story 2: Streamlined Operations

Description: We helped a medical practice achieve operational efficiency, reducing administrative costs by 25% and enhancing patient satisfaction.
Metrics: Cost savings, patient satisfaction scores, operational metrics.
Success Story 3: Data Security

Description: Our advanced security measures ensured compliance and data security for a healthcare organization, mitigating risks and enhancing trust.
Metrics: Data security compliance, risk mitigation, client feedback.
"""

if __name__ == "__main__":
    proposal_agents = createProposalAgents(agents=[admin_agent, proposal_writer_agent, proposal_critic_agent], 
                                           configs=[admin_config, proposal_writer_config, proposal_critic_config])
    proposal_group_chat = ProposalGroupChat(agents=proposal_agents, config=group_chat_config)
    # proposal_group_chat.set_human_mq(url)
    # proposal_group_chat.start_chat(stream_chatlog=True)
    proposal_group_chat.startGroupChat(input=input)