import autogen
from prompts.plan_proposal import proposal_prompt
from test_dalle import DALLEAgent
config_list_gpt4 = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4"],
    },
)

gpt4_config = {
    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list_gpt4,
    "timeout": 120,
}

config_list_dalle = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["dalle"],
    },
)

user_proxy = autogen.UserProxyAgent(
   name="Admin",
   system_message="A human admin. Interact with the planner to discuss the proposal. Plan execution needs to be approved by this admin.",
   code_execution_config=False,
)

executer = autogen.AssistantAgent(
    name="Executer",
    system_message=proposal_prompt,
    llm_config=gpt4_config,
)

critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Critic. Double check the proposal from the executer and provide feedback.",
    llm_config=gpt4_config,
)

dalle = DALLEAgent(
    name="Dalle",
    system_message="Dalle. Generate images for visual of every slide in the proposal made by the executer.",
    llm_config={"config_list": config_list_dalle}
)

groupchat = autogen.GroupChat(agents=[user_proxy, executer, critic, dalle], messages=[], max_round=50)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

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

user_proxy.initiate_chat(
    manager,
    message=input,
)