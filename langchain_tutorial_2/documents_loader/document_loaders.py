from langchain_community.document_loaders import TextLoader, BSHTMLLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.web_base import WebBaseLoader
import json
from pathlib import Path
from pprint import pprint
import time


# Loading json data
file_path='langchain_tutorial_2/documents_loader/documents/data.json'
data = json.loads(Path(file_path).read_text())
print("--------------------------JSON Data------------------------------")
pprint(data)
time.sleep(5)


# Loading HTML data
loader = BSHTMLLoader("langchain_tutorial_2/documents_loader/documents/data.html")
data = loader.load()
print("-------------------------HTML Data-------------------------")
print(data[0].page_content)
time.sleep(5)


# TextLoader to the text document
loader = TextLoader("langchain_tutorial_2/documents_loader/documents/data.txt")
data = loader.load()
print("-------------------------Text Data-------------------------")
print(data[0].page_content)
time.sleep(5)



# CSVLoader to read the CSV files
loader = CSVLoader(file_path='langchain_tutorial_2/documents_loader/documents/data.csv')
data = loader.load()
print("-------------------------CSV Data---------------------------")
print(data)
time.sleep(5)



# WebBaseLoader to load data from the webpage with URL
loader = WebBaseLoader("https://en.wikipedia.org/wiki/Virat_Kohli")
data = loader.load()
print("-------------------------Web Data---------------------------")
print(data[0].page_content[:150])