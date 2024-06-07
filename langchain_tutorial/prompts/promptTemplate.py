from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts.chat import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.5, max_tokens=1000)

template = PromptTemplate(
    template=("Write a captivating story from the perspective of a {species} who encounters a {foreign_object} for the first time. Describe their curiosity, fear, and eventual understanding. (around {count} words)"),
    input_variables=["species", "foreign_object"],
    partial_variables={"count": 75}
)


chain = template | model
response = chain.invoke({"species":"human", "foreign_object":"alien"})
print(f"response = {response}")
print(response.content)

# print(template)