from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

message = chatModel.invoke("explain langchain chat model")

print(message.content)
