'''
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def query_faiss_db(query_text: str):
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load the persisted FAISS DB
    vectorstore = FAISS.load_local(
        "faiss_db",
        embeddings=embedding,
        allow_dangerous_deserialization=True  # required when loading saved FAISS index
    )

    # Only return the single most relevant chunk
    result = vectorstore.similarity_search(query_text, k=1)[0]

    print("🔎 Query:", query_text)
    print("\n✅ Answer:")
    print(result.page_content)   # only the text, no metadata

if __name__ == "__main__":
    query_faiss_db("Leave policy")
    '''
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def query_faiss_db(query_text: str):

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "faiss_db",
        embeddings=embedding,
        allow_dangerous_deserialization=True
    )

    results = vectorstore.similarity_search(query_text, k=1)

    if not results:
        return None

    return results[0].page_content