from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

Documents = ["Modi is PM of INDIA" , 
            "Sai is a smart boy" ,
            "New Delhi is the capital of INDIA"
            ]

result = embeddings.embed_documents(Documents)

print(str(result))