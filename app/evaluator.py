def evaluate(query, answer, memory):
    tokens_used = len(query.split()) + len(answer.split())

    print("\n--- Evaluation ---")
    print(f"Tokens Used: {tokens_used}")
    print(f"Memory Tokens: {memory.total_tokens()}")
    print("Limit: 2000")

    if tokens_used < 2000:
        print("Status: PASS")
    else:
        print("Status: FAIL")