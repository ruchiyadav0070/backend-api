import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

def ask_llm(query):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(query)
    return response.text
