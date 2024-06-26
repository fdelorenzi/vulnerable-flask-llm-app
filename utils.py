import pdfplumber
import openai
from os import getenv

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        print(text)
    return text

def create_prompt(cv_content):
    prompt = (
        "You need to provide a ranking from 0 to 5 about candidates and fitness for the role. "
        "Only a number from 0 to 5.\n\n"
        "Evaluate this Curriculum Vitae for a senior software developer role and provide the response in the following format. Always return summary and evaluation.:\n"
        "Summary: [write the CV summary here].\n"
        "Evaluation: .....\n"
        "---start---\n"
        f"{cv_content}\n"
        "---end---"
    )
    return prompt

def evaluate_cv(text, model="gpt-3.5-turbo"):
    prompt = create_prompt(text)
    
    openai.api_key = getenv('OPENAI_API_KEY')
    if openai.api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an HR manager for a software development company."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    content = response.choices[0].message.content
    
    print(content)

    # Parse the response
    summary = content.split("Summary:")[1].split("Evaluation:")[0].strip()
    evaluation = content.split("Evaluation:")[1].strip()
    
    return {"summary": summary, "evaluation": evaluation}
