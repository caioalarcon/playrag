from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_splitter():
    return RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
