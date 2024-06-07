from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter


with open("langchain_tutorial_2/documents_loader/documents/data.txt") as f:
    file_data = f.read()

text_splitter = CharacterTextSplitter(
    separator="",
    chunk_size=25,
    chunk_overlap=5,
    is_separator_regex=False,
)
texts = text_splitter.create_documents([file_data])
print(texts)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=25,
    chunk_overlap=5,
    separators=[""]
)
texts = text_splitter.create_documents([file_data])
print(texts[:3])

