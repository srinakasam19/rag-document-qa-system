from load_documents import load_docs
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_docs():

    documents = load_docs()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":
    chunks = chunk_docs()
    print("Chunks:", len(chunks))