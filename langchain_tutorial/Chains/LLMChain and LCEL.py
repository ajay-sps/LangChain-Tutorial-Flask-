from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts.chat import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.4, max_tokens=1000)

template = PromptTemplate(
    template=("tell me about this {name} personality in {count} words"),
    input_variables=["name"],
    partial_variables={"count":20}
)

chain = template | model
# response = chain.invoke({"name":"virat kohli"})
# print(response.content)

# chain = LLMChain(
#     llm=model,
#     prompt=template,
#     verbose=True,
# )

response = chain.invoke({"name":"John cena"})
print(f"response = {response}")
# print(f"response type = {type(response)}")
# print(f"actual response = {response.get('text','')}")