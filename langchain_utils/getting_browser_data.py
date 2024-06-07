from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma



loader = WebBaseLoader("https://en.wikipedia.org/wiki/Virat_Kohli")
data = loader.load()

# chunks = RecursiveCharacterTextSplitter(separators=data)
chunk_size = 500
chunk_overlap = 30
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)
splits = text_splitter.split_documents(data)

embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")

# load it into Chroma
db = Chroma.from_documents(splits, embedding_function)

# query it
query = "what this webpage tells us about"
docs = db.similarity_search(query)

# print results
print(docs[0].page_content)