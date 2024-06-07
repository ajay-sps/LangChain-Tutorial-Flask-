# from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_utils.output_parser import movie_parser
from langchain.prompts import PromptTemplate
from langchain_core.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate


movie_template = "tell me {count} movies name of genre {genre} release date in {year} and the output should be in json format as defined in {format_instruction}"

movie_prompt = PromptTemplate(
    template=movie_template,
    input_variables=["genre","count","year"],
    partial_variables={
        "format_instruction":movie_parser.get_format_instructions()
    }

)

