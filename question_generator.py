from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import re

# Load model and tokenizer once
MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Use HuggingFace pipeline (optimized internally)
question_generator = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,
    temperature=0.7,
    do_sample=True
)

def clean_output(text):
    # Split and clean multi-line output
    lines = text.split("\n")
    questions = []
    for line in lines:
        line = re.sub(r"^\s*[-\d\.\)]\s*", "", line).strip()
        if line and "?" in line:
            questions.append(line)
    return questions

def generate_questions(description: str, num_questions: int = 3):
    prompt = (
        f"You are an expert assistant helping to complete product information forms for an e-commerce platform.\n\n"
        f"Given a product description, your job is to ask a few intelligent, concise, and specific follow-up questions. "
        f"These questions should help gather missing details, clarify vague information, or improve the completeness of the product listing.\n\n"
        f"Only ask questions that are relevant and not already answered. Avoid yes/no questions and focus on helpful product-specific details like specifications, features, materials, certifications, compatibility, usage, etc.\n\n"
        f'Product Description:\n"{description}"\n\n'
        f"Ask {num_questions} follow-up questions:"
    )
    response = question_generator(prompt)[0]['generated_text']
    return clean_output(response)
