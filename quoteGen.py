from apiKey import api
import openai

openai.api_key = (api)

def quoteGen(title):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"find a quote relevant to synchronicity for a blog post:“In synchronicity we are recognizing our own nature” -Deepak Chopra###\nfind a quote relevant to {title} for a blog post:",
      temperature=0.58,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0.59,
      presence_penalty=0.32,
      stop=["###"]
    )

    return response["choices"][0]["text"]
