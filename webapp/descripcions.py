import openai

openai.api_key = 'sk-proj-kFIaBVsdYPM9VKtlLC8sT3BlbkFJRahplEZyfzb35x0Q5LPH'

lloc = "Londres"

text = "I want a json of places to visit in "+lloc+" 'name', 'short description', 'long description','budget in euros'(value) 'type of plan ([culture,history,science,familiar,relax,party,shopping,outdoors activities])'"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": text}]
)
print(response.choices[0].message.content)