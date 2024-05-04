import openai
from openai import OpenAI

openai.api_key = 'sk-proj-Ym9QzZuk5v9OUDJXBz5rT3B1bkFJ4oLG5Ao'
client = OpenAI()
lloc = "Londres"

text = "I want a json of places to visit in "+lloc+" 'name', 'short description', 'long description','budget in euros'(value) 'type of plan ([culture,history,science,familiar,relax,party,shopping,outdoors activities])'"

response = client.chat.completions.create(
  model="gpt-4",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": text}]
)
print(response.choices[0].message.content)