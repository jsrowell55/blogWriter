from apiKey import api
import openai

openai.api_key = (api)


def BOGen(title, subtitle):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"create an outline for the body of a blog post titled 'What is Synchronicity?' with 3 or 4 sections-->What is synchronicity?\nSynchronicity vs Coincidence\nExplanations for synchronicity###\ncreate an outline for the body of a blog post titled 'How to Manifest Your Desires Into Reality' with 3 or 4 sections:Understand what you desire\nVisualize your desires as already being reality\nTake action towards your desires\nLet go of attachment to the outcome###\ncreate an outline for the body of a blog post titled 'The Search for Meaning : and how it can help us find our way in the world' with 3 or 4 items-->What is the search for meaning?\nHow can the Search for Meaning help us find our way in the world?\nTips for search for meaning\nThe role of meaning in our lives###\ncreate an outline for the body of a blog post titled 'The Universe is Alive : and how we can change it through our thoughts and actions' with 3 or 4 items-->The universe is alive and supportive of our highest good\nWe can change the universe through our thoughts and actions\nWhen we live in alignment with the universe, we experience more synchronicity and flow\nChanging our lives for the better starts with changing our thoughts and actions###\ncreate an outline for the body of a blog post titled '{title} : {subtitle}' with 3 or 4 items-->",
      temperature=1,
      max_tokens=256,
      top_p=1,
      best_of=2,
      frequency_penalty=1.5,
      presence_penalty=1.5,
      stop=["###", "-->"]
    )

    return response["choices"][0]["text"]
