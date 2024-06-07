from langchain_utils.llm_model import llm_model
from langchain_utils.output_parser import movie_parser
from langchain_utils.prompt_template import movie_prompt


movie_chain = movie_prompt | llm_model | movie_parser