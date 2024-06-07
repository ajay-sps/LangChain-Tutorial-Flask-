from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts.chat import PromptTemplate


model = ChatOpenAI()

class PlayerDetails(BaseModel):
    date_of_birth : str = Field()
    birth_place : str = Field()
    total_matches : int = Field()
    description : str = Field()

pydantic_parser = PydanticOutputParser(pydantic_object=PlayerDetails)
json_parser = JsonOutputParser()
template = "give me the details of sportperson {name} as per {instruction_format}"

prompt = PromptTemplate(
    template=template,
    input_variables=["name"],
    partial_variables={
        "instruction_format": pydantic_parser.get_format_instructions()
    }
)

chain = prompt | model | json_parser
response = chain.invoke({"name":"sachin tendulkar"})
print(f"response = {response}")

