from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", dimensions = 300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about Virat Kohli"

documents_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

print(cosine_similarity([query_embedding] , documents_embedding))