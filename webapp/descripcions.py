from groq import Groq

def read_api_key(file_path):
  with open(file_path, "r") as file:
    api_key = file.read().strip()
    return api_key

client = Groq(
# Lee la API key del archivo
  api_key = read_api_key("C:/Users/weiha/Documents/API_KEY.txt")
)

lloc = "Londres"
text = "I want a json of places to visit in "+lloc+" 'name', 'short description', 'long description','budget in euros'(value) 'type of plan ([culture,history,science,familiar,relax,party,shopping,outdoors activities])'"

chat_completion = client.chat.completions.create(
    messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": text}
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)