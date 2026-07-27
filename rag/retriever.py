import chromadb
from chromadb.utils import embedding_functions

def query_knowledge_base(query_text, n_results=3):
    client = chromadb.PersistentClient(path="rag/chroma_db")
    
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    collection = client.get_collection(
        name="phishing_knowledge_base",
        embedding_function=embedding_fn
    )
    
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    
    return results


if __name__ == "__main__":
    test_queries = [
        "email asking to verify account urgently",
        "suspicious domain with numbers instead of letters",
        "email claiming I won a prize",
        "link that redirects multiple times",
        "email requesting my password directly"
    ]
    
    for query in test_queries:
        print(f"\n{'='*60}")
        print(f"QUERY: {query}")
        print('='*60)
        results = query_knowledge_base(query, n_results=2)
        for i, doc in enumerate(results['documents'][0]):
            doc_id = results['ids'][0][i]
            print(f"\n[Match {i+1}: {doc_id}]")
            print(doc[:150] + "...")