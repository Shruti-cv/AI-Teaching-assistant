from transformers import pipeline

# Load lightweight text generation model
generator = pipeline("text-generation", model="distilgpt2")

def refine_intent_with_llm(query, predicted_intent):

    prompt = f"""
    You are an AI teaching assistant.
    A student asked: "{query}"
    The predicted intent is: "{predicted_intent}".

    Confirm if this intent is correct.
    If incorrect, suggest the correct one from:
    [Explanation, Example, Doubt, Revision].

    Return only one word.
    """

    response = generator(prompt, max_length=100, num_return_sequences=1)

    generated_text = response[0]["generated_text"]

    # Simple extraction logic
    for intent in ["Explanation", "Example", "Doubt", "Revision"]:
        if intent.lower() in generated_text.lower():
            return intent

    return predicted_intent
