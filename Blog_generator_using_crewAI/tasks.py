from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points."
        "its market opportunities, and potenial risks."
    ),
    expected_output = 'A comprehensive report on the next big trend in {topic}.',
    tools=[tool],
    agent=news_researcher
)

write_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand and engaging."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post-programming.md'
)