from apiKey import api
from titleGen import titleGen
import openai

openai.api_key = (api)

def introGen(title):
    with open(title, "r") as post:
        post = post.read()
        post = post.replace("\n", " ")

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"Create an introduction paragraph to a blog post about synchronicity:What is Synchronicity? : and how can it teach us about the world outside our minds? The following was written by an AI “In synchronicity we are recognizing our own nature” -Deepak Chopra :: There’s something both mysterious and magical about synchronicity. It’s as if the universe is conspiring to send us a message. Whether it’s a chance meeting with a stranger or a series of events that seem to be connected, synchronicity often leaves us feeling amazed and bewildered. While the concept of synchronicity is often associated with positive experiences, it can also occur during difficult times. For example, you might suddenly find yourself thinking about someone you haven’t seen in years right before they walk into the room. Or you might have a dream about an upcoming event that later comes true. Synchronicity can be interpreted in many different ways, but one thing is certain: it’s a reminder that we’re all connected in ways we may not always be able to understand.###\nCreate an introduction paragraph to a blog post about {title} : {post} ::",
      temperature=0.9,
      max_tokens=300,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["###"]
    )

    return response["choices"][0]["text"]
