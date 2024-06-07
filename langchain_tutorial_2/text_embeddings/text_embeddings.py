from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


embedding_model = OpenAIEmbeddings()

raw_documents = TextLoader("langchain_tutorial_2/documents_loader/documents/data.txt").load()
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(raw_documents)


embeddings = embedding_model.embed_documents(documents[0].page_content)
print(embeddings)