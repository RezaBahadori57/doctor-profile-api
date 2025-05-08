from openai import OpenAI
import os

from streamlit import secrets

# for used from V2Ray proxy
os.environ["HTTP_PROXY"] = "http://127.0.0.1:2080"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:2080"

name = input("Input your sentence: ")
print( name)



client = OpenAI(api_key=secrets["OPENAI_API_KEY"])

response = client.embeddings.create(
    input=name,
    model="text-embedding-3-small"
)

print(response.data[0].embedding)