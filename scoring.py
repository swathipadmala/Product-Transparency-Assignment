def compute_score(description: str):
    # Simple rule-based logic; you can improve using LLM scoring later
    word_count = len(description.split())
    score = min(100, word_count * 2)  # e.g., 50 words => 100%
    return {"score": score, "feedback": "Looks detailed!" if score > 70 else "Consider adding more details."}
