from apiKey import api
import openai

openai.api_key = (api)


def BPGen(title, part):
    with open(title, "r") as post:
        post = post.read()
        post = post.replace("\n", " ")

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"continue the following blog post about synchronicity, by writing a paragraph about \"Synchronicity vs Coincidence\": What is Synchronicity? : and how can it teach us about the world outside our minds? The following was written by an AI “Synchronicity” — NightCafe “In synchronicity we are recognizing our own nature” -Deepak Chopra :: There’s something both mysterious and magical about synchronicity. It’s as if the universe is conspiring to send us a message. Whether it’s a chance meeting with a stranger or a series of events that seem to be connected, synchronicity often leaves us feeling amazed and bewildered. While the concept of synchronicity is often associated with positive experiences, it can also occur during difficult times. For example, you might suddenly find yourself thinking about someone you haven’t seen in years right before they walk into the room. Or you might have a dream about an upcoming event that later comes true. Synchronicity can be interpreted in many different ways, but one thing is certain: it’s a reminder that we’re all connected in ways we may not always be able to understand.It is often said that life is full of coincidences. But what exactly is a coincidence? And what is the difference between a coincidence and synchronicity? A coincidence is defined as two or more events that happen at the same time by chance. So, if you bump into a friend you haven’t seen in years on the street, that would be considered a coincidence. Synchronicity, on the other hand, is defined as two or more events that are meaningful and related to each other. So, if you have been thinking about a friend you haven’t seen in years and then you bump into them on the street, that would be considered synchronicity. There are many theories as to why synchronicities occur, but one thing is for sure — they often leave us feeling amazed, connected, and hopeful.###continue the following blog post about {title}, by writing a paragraph about \"{part}\": {post} ::",
      temperature=0.8,
      max_tokens=2000,
      top_p=1,
      frequency_penalty=1.9,
      presence_penalty=0,
      stop=["###"]
    )

    return response["choices"][0]["text"]
