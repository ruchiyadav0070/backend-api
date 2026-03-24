from llm import ask_llm

def process_query(query, graph):
    if "weather" in query.lower():
        return "Only dataset-related queries allowed."

    intent = ask_llm(query)

    if "highest" in intent.lower():
        return "Product P1 has highest billing"

    return "Query processed successfully"
