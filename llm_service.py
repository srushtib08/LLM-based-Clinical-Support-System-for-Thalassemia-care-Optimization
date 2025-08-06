import openai

openai.api_key = "your_api_key"

def get_llm_response(prompt: str) -> str:
    messages = [
        {"role": "system", "content": "You are an assistant specializing in thalassemia management."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
    return response['choices'][0]['message']['content']
