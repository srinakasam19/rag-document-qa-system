from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_docs():

    folder_path = r"C:\Users\KasamLaxmiSrina\Documents\rag aiml hitachi\documents"

    loader = DirectoryLoader(
        folder_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()

    return documents