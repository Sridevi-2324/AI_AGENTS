from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

news_researcher=Agent(
    role="Senior Researcher",
    goal="To provide the best research and insights to the team on {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "I have been a researcher for over 10 years." 
        "I have worked on a variety of topics from AI."
        "I am passionate about learning and sharing knowledge with others."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

news_writer=Agent(
    role='Writer',
    goal='To write the best articles on {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "I have been a writer for over 5 years."
        "I have written articles on a variety of topics from AI."
        "I am passionate about writing and sharing knowledge with others."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)