"""
Custom agent for generating AI fluency plans.
Uses OpenAI LLM via LangChain with a simple prompt template.
"""

from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import os

# Ensure the OpenAI API key is set in environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY environment variable not set. "
        "Please set it before using the agent."
    )

# Configure the LLM (ChatGPT)
llm = ChatOpenAI(temperature=0.7, model_name="gpt-4o-mini")

# Prompt template for generating a structured plan
prompt_template = """
You are an expert AI fluency coach. Based on the following user context,
create a detailed personal AI fluency plan that covers the four stages:
Awareness, Understanding, Application, and Mastery.
Include goals, learning resources, milestones, assessment methods,
and reflection checkpoints.

User Context: {user_input}

Provide the plan in Markdown format with clear headings for each stage.
"""

prompt = PromptTemplate(
    input_variables=["user_input"],
    template=prompt_template
)

# Build the chain
chain = LLMChain(llm=llm, prompt=prompt)

def generate_fluency_plan(user_input: str) -> str:
    """
    Generate a fluency plan given user context.

    Parameters
    ----------
    user_input : str
        Description of user's goals, background, or desired outcomes.

    Returns
    -------
    str
        The generated plan in Markdown format.
    """
    if not user_input.strip():
        raise ValueError("User input must be a non-empty string.")
    result = chain.run({"user_input": user_input})
    return result
