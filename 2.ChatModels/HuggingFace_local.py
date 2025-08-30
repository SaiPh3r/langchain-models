from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

# Step 1: Create the Hugging Face pipeline
generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200,
    temperature=0.7,
    do_sample=True
)

# Step 2: Wrap inside HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=generator)

# Step 3: Convert to chat model
chat_model = ChatHuggingFace(llm=llm)

# Step 4: Invoke
result = chat_model.invoke("Who is the president of India?")
print(result.content)