from scraper import get_data

def get_rag_answer(query):
    data = get_data()
    return f"RAG Answer based on scraped data: {data[:100]}..."
