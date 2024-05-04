import openai

openai.api_key = 'sk-proj-Ym9QzZuk5v9OUDJXBz5rT3B1bkFJ4oLG5Ao'

lloc = "Londres"

response = openai.ChatCompletion.create(
  model="gpt-4",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": f"I want a json of places to visit in {lloc}"},
    ]
)
print(response.choices[0].message.content)