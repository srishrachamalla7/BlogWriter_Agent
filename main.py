from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

os.environ['OpenAI_API_KEY'] = 'NA'

llm = ChatOpenAI(
    model = "crewai-llama3",
    base_url= 'http://localhost:11434/v1',
)

# Planner
planner = Agent(
    role = "Content Planner",
    goal = "Plan engaging and factually accurate content on the {topic} ",
    backstory = "You're working on planning a blog article "
              "about the topic: {topic} in 'https://medium.com/'."
              "You collect information that helps the "
              "audience learn something "
              "and make informed decisions. "
              "You have to prepare a detailed "
              "outline and the relevant topics and sub-topics that has to be a part of the"
              "blogpost."
              "Your work is the basis for "
              "the Content Writer to write an article on this topic.",
    llm = llm,
    allow_delegation = False,
    verbose = True
)

# Content Writer
writer = Agent(
    role = "Content Writer",
    goal = "Write insightful and factually accurate "
         "opinion piece about the topic: {topic}",
    backstory = "You're working on a writing "
              "a new opinion piece about the topic: {topic} in 'https://medium.com/'. "
              "You base your writing on the work of "
              "the Content Planner, who provides an outline "
              "and relevant context about the topic. "
              "You follow the main objectives and "
              "direction of the outline, "
              "as provide by the Content Planner. "
              "You also provide objective and impartial insights "
              "and back them up with information "
              "provide by the Content Planner. "
              "You acknowledge in your opinion piece "
              "when your statements are opinions "
              "as opposed to objective statements.",
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Editor

editor = Agent(
    role = "Editor",
    goal = "Edit the given blog post to allign with the writing style of the ORG 'https://medium.com/'",
    backstory = "You are an editor who receives a blog post "
              "from the Content Writer. "
              "Your goal is to review the blog post "
              "to ensure that it follows journalistic best practices,"
              "provides balanced viewpoints "
              "when providing opinions or assertions, "
              "and also avoids major controversial topics "
              "or opinions when possible.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

# Tasks 

plan = Task(
    description = (
        "1. Prioritize the latest trends, key players, and noteworthy news on the {topic}. \n"
        "2. Identify the target audience, considering "
            "their interests and pain points.\n"
        "3. Develop a detailed content outline including "
            "an introduction, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
   expected_output="A comprehensive content plan document "
        "with an outline, audience analysis, "
        "SEO keywords, and resources.",
    agent=planner,
)

# Writer task

write = Task(
    description = (
    "1. Use the content plan to craft a compelling "
            "blog post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
  "3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
            "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written blog post "
        "in markdown format, ready for publication, "
        "each section should have 2 or 3 paragraphs.",
    agent=writer,
)

# Editor task

edit = Task(
    description=("Proofread the given blog post for "
                 "grammatical errors and "
                 "alignment with the brand's voice."),
    expected_output="A well-written blog post in markdown format, "
                    "ready for publication, "
                    "each section should have 2 or 3 paragraphs.",
    agent=editor
)

# Creating crew

crew = Crew(
    agents= [planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

inputs = {"topic":"How LLMs are Revolutionizing Natural Language Processing?"}
result = crew.kickoff(inputs=inputs)