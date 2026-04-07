def generate_answer(query, context_list):
    context = "\n".join(f"- {c}" for c in context_list)

    return f"""
Final Answer (Simulated LLM):

Query:
{query}

Key Insights:
{context}

Structured Analysis:

1. United States:
- Higher production cost
- Strong regulatory environment

2. China:
- Dominates raw materials and manufacturing
- Risk of geopolitical dependency

3. Europe:
- Focus on sustainability and regulation
- Supply chain still developing

Conclusion:
Each region presents trade-offs between cost, control, and resilience.
"""