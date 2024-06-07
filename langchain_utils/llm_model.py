from langchain_openai import ChatOpenAI
from langchain_utils.get_json_data import data
from dotenv import load_dotenv
load_dotenv()


model_name = data.get('model_data').get("model")
max_tokens = data.get('model_data').get("max_tokens")
temperature = data.get('model_data').get("temperature")

llm_model = ChatOpenAI(
            model_name=model_name, max_tokens=max_tokens, temperature=temperature
        )