from chunk import chunk_docs
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def create_chroma_db():
    # load chunks
    chunks = chunk_docs()

    # load embedding model (updated import)
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # create Chroma DB
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="chroma_db"
    )

    print("✅ Chroma DB created successfully")

if __name__ == "__main__":
    create_chroma_db()