from chunk import chunk_docs
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def create_faiss_db():
    # load chunks
    chunks = chunk_docs()

    # load embedding model
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # create FAISS DB
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embedding
    )

    # save FAISS index locally
    vectorstore.save_local("faiss_db")

    print("✅ FAISS DB created successfully")

if __name__ == "__main__":
    create_faiss_db()