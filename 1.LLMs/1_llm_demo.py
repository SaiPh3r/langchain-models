from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load variables from .env
load_dotenv()

# LangChain automatically picks GOOGLE_API_KEY from environment
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

response = llm.invoke("What is the capital of India?")
print(response.content)