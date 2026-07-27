import os
import chromadb
from chromadb.utils import embedding_functions

def load_documents(folder_path="rag/knowledge_base"):
    documents = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                documents.append(f.read())
                filenames.append(filename)
    return documents, filenames

def build_vector_store():
    documents, filenames = load_documents()
    
    client = chromadb.PersistentClient(path="rag/chroma_db")
    
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    collection = client.get_or_create_collection(
        name="phishing_knowledge_base",
        embedding_function=embedding_fn
    )
    
    collection.add(
        documents=documents,
        ids=filenames
    )
    
    print(f"Added {len(documents)} documents to vector store.")
    return collection


if __name__ == "__main__":
    build_vector_store()