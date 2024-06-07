from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


model = ChatOpenAI(temperature=0.9)

query = "Tell me an interesting fact about animals."
parser = JsonOutputParser()

prompt = PromptTemplate(
    template="{query} as {format_instructions}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

response = chain.invoke({"query": query})
print(response)
