from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.vectorstores import faiss


embedding_model = OpenAIEmbeddings()

raw_documents = TextLoader("langchain_tutorial_2/documents_loader/documents/data.txt").load()
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(raw_documents)


vector = faiss.FAISS.from_documents(documents, embedding_model)
data = vector.similarity_search("kohli")
print(data[0].page_content)
