# rag.py
import os
os.environ["GOOGLE_API_KEY"] = "............"
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from query import query_faiss_db


def rag_query(question: str):

    # 1️⃣ Retrieve context from FAISS
    context = query_faiss_db(question)

    if context is None:
        print("No relevant information found.")
        return

    # 2️⃣ Initialize Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.3
    )

    # 3️⃣ Prompt Template
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful assistant.
    Answer the question based only on the provided context.

    Context:
    {context}

    Question:
    {question}
    """)

    formatted_prompt = prompt.format(
        context=context,
        question=question
    )

    # 4️⃣ Generate response
    response = llm.invoke(formatted_prompt)

    print("🔎 Question:", question)
    print("\n📚 Retrieved Context:")
    print(context)
    print("\n🤖 Final Answer:")
    print(response.content)


if __name__ == "__main__":
    rag_query("leave policy")