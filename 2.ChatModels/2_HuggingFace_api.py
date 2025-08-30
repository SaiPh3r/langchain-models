from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "Qwen/Qwen3-Coder-480B-A35B-Instruct" ,
    task= "text-generation" , 
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("who is pm of india")

print(result.content)