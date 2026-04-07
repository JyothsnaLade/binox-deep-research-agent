from planner import decompose_query
from retriever import retrieve_docs
from memory import MemoryManager
from generator import generate_answer
from evaluator import evaluate

def run_agent(query):
    print(f"\nQuery: {query}\n")

    sub_queries = decompose_query(query)

    memory = MemoryManager(token_limit=2000)

    context_chunks = []

    for sub_q in sub_queries:
        docs = retrieve_docs(sub_q)
        compressed = memory.add_and_compress(docs)
        if compressed not in context_chunks:
            context_chunks.append(compressed)

    answer = generate_answer(query, context_chunks)

    evaluate(query, answer, memory)

    return answer


if __name__ == "__main__":
    query = "Compare EV battery supply chain risks across US, China, and EU"
    result = run_agent(query)
    print("\nFinal Answer:\n", result)