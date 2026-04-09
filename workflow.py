from rag import get_rag_answer
from serp_tool import get_web_answer

def route(query):
    if "debales" in query.lower():
        return "rag"
    elif "what" in query.lower() or "who" in query.lower():
        return "serp"
    else:
        return "mixed"

def run_agent(query):
    decision = route(query)

    if decision == "rag":
        return get_rag_answer(query)
    elif decision == "serp":
        return get_web_answer(query)
    else:
        rag = get_rag_answer(query)
        web = get_web_answer(query)
        return f"{rag}\n\nAdditional info:\n{web}"
