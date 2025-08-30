from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

# Load variables from .env
load_dotenv()

# Plain LLM (not chat) - like OpenAI's "instruct" models
llm = GoogleGenerativeAI(model="gemini-1.5-flash")

result = llm.invoke("What is the capital of India?")
print(result)