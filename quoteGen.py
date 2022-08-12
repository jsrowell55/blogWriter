from apiKey import api
import openai

openai.api_key = (api)

def quoteGen(title, subtitle):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"find a quote relevant to a blog post titled 'What is Synchronicity? : And how can it teach us about the world outside our minds?'-->“In synchronicity we are recognizing our own nature” -Deepak Chopra###\nfind a quote relevant to a blog post titled 'The Secret of Alchemy : Uncovering the Mysterious Process That Transforms Matter'-->\"There is nothing more difficult to carry out, nor more doubtful of success, nor more dangerous to handle, than to initiate a new order of things.\" -Machiavelli###\nfind a quote relevant to a blog post titled 'The Power of Forgiveness : How to let go of resentment and find inner peace'-->\"Forgiveness is the key that unlocks the door to freedom.\" -Colin Tipping###\nfind a quote relevant to a blog post titled '{title} : {subtitle}'-->",
      temperature=0.8,
      max_tokens=256,
      top_p=1,
      frequency_penalty=1.3,
      presence_penalty=1,
      stop=["###", "-->"]
    )

    return response["choices"][0]["text"]
