from apiKey import api
import openai

openai.api_key = (api)

def titleGen():
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="create a title and a subtitle for a blog post from a blog that discusses topics like, spirituality, magic, psychedelics, symbology, religion, eastern yoga, and mythology - What is Synchronicity? : and how can it teach us about the world outside our minds?###\ncreate a title and a subtitle for a blog post from a blog that discusses topics like the occult, spirituality, magic, psychedelics, symbology, religion, eastern yoga, and mythology - The Difference Between Religion and Spirituality : and how to find your path###\ncreate a title and a subtitle for a blog post from a blog that discusses topics like, spirituality, magic, psychedelics, symbology, religion, eastern yoga, and mythology - The mythology of Shiva : and how he can teach us about the nature of reality###\ncreate a title and a subtitle for a blog post from a blog that discusses topics like, spirituality, magic, psychedelics, symbology, religion, eastern yoga, and mythology - The Personification of DMT : Who is Hakini Shakti?###\ncreate a title and a subtitle for a blog post from a blog that discusses topics like, spirituality, magic, psychedelics, symbology, religion, eastern yoga, and mythology -",
      temperature=0.9,
      max_tokens=256,
      top_p=1,
      frequency_penalty=1.5,
      presence_penalty=0,
      stop=["###"]
    )

    return response["choices"][0]["text"]
