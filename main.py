from fastapi import FastAPI
from pydantic import BaseModel
from app.question_generator import generate_questions
from app.scoring import compute_score

app = FastAPI()

class ProductDescription(BaseModel):
    description: str

@app.post("/generate-questions")
def ask_questions(product: ProductDescription):
    questions = generate_questions(product.description)
    return {"questions": questions}

@app.post("/transparency-score")
def get_score(product: ProductDescription):
    return compute_score(product.description)
