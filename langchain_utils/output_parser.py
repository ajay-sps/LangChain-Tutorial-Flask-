from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator


class MovieDetails(BaseModel):
    name: str = Field (description="it tell us the movie name")
    release_date: str = Field(description="it tell us the release_date of movie")
    director : str = Field(description="tell us the director of the movie")
    collection : str = Field(description="tell us the collection of the movie")


class Movies(BaseModel):
    movies : list[MovieDetails] = Field(description="contains the list of the movies")


movie_parser = PydanticOutputParser(pydantic_object=Movies)

