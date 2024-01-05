from proposal.configs import *
from proposal.agents import *
from proposal.group_chat import ProposalGroupChat
from design.configs import *
from design.agents import *
from design.group_chat import ProposalDesignGroupChat
from finalize_proposal.configs import *
from finalize_proposal.agents import *
from finalize_proposal.group_chat import ProposalFinalizeGroupChat
from organization.org_chart import ProposalOrgChart
from organization.configs import org_chart_config

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
    proposal_agents = createProposalAgents(agents=[proposal_admin_agent, proposal_writer_agent, proposal_critic_agent], 
                                           configs=[proposal_admin_config, proposal_writer_config, proposal_critic_config])
    design_agents = createProposalAgents(agents=[retrieval_admin_agent, visualizer_agent, designer_agent], 
                                         configs=[retrieval_admin_config, visualizer_config, designer_config])
    finalize_agents = createProposalAgents(agents=[finalize_admin_agent, proposal_finalizer_agent], 
                                           configs=[finalize_admin_config, proposal_finalizer_config])
    
    proposal_group_chat = ProposalGroupChat(agents=proposal_agents, config=group_chat_config)
    design_group_chat = ProposalDesignGroupChat(agents=design_agents, config=group_chat_config)
    finalize_group_chat = ProposalFinalizeGroupChat(agents=finalize_agents, config=group_chat_config)

    proposal_team = proposal_group_chat.formTeam(name="Proposal", 
                                 feature="Develop and write the initial content for the slide deck, focusing on key messages, project objectives, and essential information.", 
                                 deliverable="A draft of the slide deck with text content, including notes on suggested imagery.", 
                                 communication="Share the draft content with the Design Team for visual enhancement."
                                 )
    
    design_team = design_group_chat.formTeam(name="Design",
                                 feature="Design and provide relevant images, graphics, and visual elements that complement and enhance the textual content from the Proposal Team.",
                                 deliverable="A set of images and graphic elements tailored to fit the proposed slide content.",
                                 communication="Provide the designed images and graphics to the Finalize Team for slide deck assembly."
                                 )
    finalize_team = finalize_group_chat.formTeam(name="Finalize",
                                 feature="Integrate the content from the Proposal Team and the images from the Design Team into a final, cohesive slide deck.",
                                 deliverable="The completed slide deck, ready for review and presentation.",
                                 communication="Present the final slide deck to the Proposal and Design Teams for feedback and approval."
                                 )
    org_chart = ProposalOrgChart(epic="Enable efficient collaboration among the Proposal Team, Design Team, and Finalize Team to develop a comprehensive and visually appealing slide deck for project presentations.", 
                                 teams=[proposal_team, design_team, finalize_team], config=org_chart_config
                                 )

    org_chart.startUp(input=input)
    
    # proposal_group_chat.startGroupChat(input=input)
    # design_group_chat.startGroupChat(input="""Generate images for the proposal.""")
    # finalize_group_chat.startGroupChat(input=input)
