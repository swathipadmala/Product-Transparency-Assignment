# Product-Transparency-Assignment
# Product Description Assistant

An open-source FastAPI microservice that intelligently enhances product descriptions. It uses local AI models to:
- Generate clarifying questions
- Score the transparency of product descriptions
- Work without any OpenAI API keys

# Features

- **AI-Powered Question Generation**  
  Uses open-source LLMs (like `flan-t5-base`) to ask follow-up questions based on the product description.

-**Transparency Scoring**  
  Computes a score indicating how informative the product description is.

-**LLM-Only Backend**  
  No rule-based logic or hardcoded questions.

-**Offline-Friendly**  
  Works entirely with local models (no OpenAI API needed).

- **Modular & Lightweight**  
  Built with FastAPI. Easy to integrate into other systems.

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Swathipadmala/product_QA.git
cd product_QA

main.py,question_generator.py,scoring.py should be in app folder

2. Create and activate a virtual environment
bash
Copy code
python -m venv env
env\Scripts\activate     # Windows
# OR
source env/bin/activate  # macOS/Linux

3. Install dependencies
bash
Copy code
pip install -r requirements.txt
Make sure torch and transformers are included in requirements.txt.

4. Start the API server
bash
Copy code
uvicorn app.main:app --reload
Open your browser to: http://127.0.0.1:8000/docs


 API Documentation
 POST /generate-questions
Generates clarifying questions to improve a product description.


Request Body:

json
Copy code
{
  "description": "A Bluetooth speaker with 10 hours of battery life."
}


Response:

json
Copy code
{
  "questions": [
    "Is the speaker waterproof or splash resistant?",
    "Does it support stereo pairing with another speaker?",
    "What is the Bluetooth version and range?"
  ]
}



 POST /transparency-score
Evaluates how clear and informative the product description is.

Request Body:

json
Copy code
{
  "description": "Noise-cancelling headphones with 40-hour battery, USB-C fast charging, and Google Assistant support."
}


Response:

json

{
  "score": 92,
  "feedback": "The description is informative and covers features, usage, and compatibility."
}
 Sample Input + Output
 Sample Product:
“An ergonomic office chair with mesh back, adjustable armrests, and lumbar support.”



 Generated Questions:
What is the maximum weight capacity of the chair?

Does it offer tilt and recline adjustment?

Is it easy to assemble and does it come with a warranty?

 Transparency Score:
json
{
  "score": 85,
  "feedback": "Well-written, but consider adding material quality or warranty info."
}



 Requirements.txt
nginx
Copy code
fastapi
uvicorn
transformers
torch
Model used: google/flan-t5-base (downloaded from HuggingFace)



 Reflection
How did you use AI tools in development?
We used HuggingFace Transformers with flan-t5-base to handle prompt-based question generation. All questions are LLM-generated in real time, conditioned on the product description. This avoids static templates and makes the system adaptable to new product types.

What principles guided your architecture and transparency logic?
We focused on openness, modularity, and explainability. The goal was to empower users to create better product listings through gentle, model-driven nudges. Our transparency score is qualitative and focused on completeness, usability, and clarity — traits aligned with ethical product disclosure and trust-building in ecommerce.
