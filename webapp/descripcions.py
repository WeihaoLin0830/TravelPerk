from groq import Groq

client = Groq(
    api_key="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",
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