from langchain_openai.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain_core.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.4, max_tokens=1000)


# template = ChatPromptTemplate(
#     messages=[
#         SystemMessagePromptTemplate.from_template("You are a travel consultant with expertise in different tourists places and your name is Ritik and you need to tell the tourists places for this city {location} in {count} words"),
#         HumanMessagePromptTemplate.from_template("{location}"),
#     ],
#     input_variables=["location"],
#     partial_variables={
#         "count":75,
#     }
# )

template = ChatPromptTemplate( 
    messages=[
        SystemMessagePromptTemplate.from_template("You are a helpful AI bot. Your name is {name}."),
        HumanMessagePromptTemplate.from_template("Hello, how are you doing?"),
        AIMessagePromptTemplate.from_template("I'm doing well, thanks!"),
        HumanMessagePromptTemplate.from_template("{user_input}"),
    ],
    input_variables=["user_input"],
    partial_variables={
        "name": "Alice",
    },
)

chain = template | model

# response = chain.invoke({"location":"chandigarh"})
response = chain.invoke({"user_input":"who are you and what you can do"})
# print(f"resposne = {response}")
print(response.content)




# print(f"chain = {chain}")
# print(f"response = {response}")
# chain = LLMChain(
#     llm=model,
#     prompt=template,
#     verbose=True
# )