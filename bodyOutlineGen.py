from apiKey import api
import openai

openai.api_key = (api)

def BOGen(title):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"create an outline for the body of a blog post about synchronicity with 3 or 4 items:What is synchronicity?\nSynchronicity vs Coincidence\nExplanations for synchronicity###\ncreate an outline for the body of a blog post about {title} with 3 or 4 items:",
      temperature=1,
      max_tokens=256,
      top_p=1,
      best_of=3,
      frequency_penalty=1.5,
      presence_penalty=0,
      stop=["###"]
    )

    return response["choices"][0]["text"]
