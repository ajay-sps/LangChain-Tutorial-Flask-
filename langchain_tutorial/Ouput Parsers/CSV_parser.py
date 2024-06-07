from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


model = ChatOpenAI(temperature=0.5)

query = "Ice-Cream Flavour"
parser = CommaSeparatedListOutputParser()


prompt = PromptTemplate(
    template="List ten. {query}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


chain = prompt | model 

response = chain.invoke({"query": query})
print(f"response = {response}")