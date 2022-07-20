from apiKey import api
import openai

openai.api_key = (api)

def conclusionGen(title):
    with open(title, "r") as post:
        post = post.read()
        post = post.replace("\n", " ")

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"write a conclusion paragraph for the following blog post about synchronicity:What is Synchronicity? and how can it teach us about the world outside our minds? The following was written by an AI “In synchronicity we are recognizing our own nature” -Deepak Chopra There’s something both mysterious and magical about synchronicity. It’s as if the universe is conspiring to send us a message. Whether it’s a chance meeting with a stranger or a series of events that seem to be connected, synchronicity often leaves us feeling amazed and bewildered. While the concept of synchronicity is often associated with positive experiences, it can also occur during difficult times. For example, you might suddenly find yourself thinking about someone you haven’t seen in years right before they walk into the room. Or you might have a dream about an upcoming event that later comes true. Synchronicity can be interpreted in many different ways, but one thing is certain: it’s a reminder that we’re all connected in ways we may not always be able to understand. What is synchronicity? Synchronicity is a term coined by psychologist Carl Jung to describe the phenomenon of two or more events that are seemingly unrelated occurring together in a meaningful way. Jung believed that synchronicity was a sign that the universe was trying to communicate with us, and that these coincidences were actually meaningful messages. He also believed that synchronicity could be used as a tool for personal growth and transformation. Synchronicity can manifest in many different ways, but some common examples include: Meeting someone randomly and then discovering that you have a lot in common Hearing a song on the radio that seems to be speaking directly to your current situation Suddenly remembering something important just when you need it If you believe that synchronicity is at work in your life, pay attention to the signs and see what message they might be trying to tell you! Synchronicity vs Coincidence It is often said that life is full of coincidences. But what exactly is a coincidence? And what is the difference between a coincidence and synchronicity? A coinciden ce is defined as two or more events that happen at the same time by chance. So, if you bump into a friend you haven’t seen in years on the street, that would be considered a coincidence. Synchronicity, on the other hand, is defined as two or more events that are meaningful and related to each other. So, if you have been thinking about a friend you haven’t seen in years and then you bump into them on the street, that would be considered synchronicity. There are many theories as to why synchronicities occur, but one thing is for sure — they often leave us feeling amazed, connected, and hopeful. Explanations for synchronicity There are a number of possible explanations for synchronicity, including: The law of attraction: This theory suggests that like attracts like, and that synchronicities are a manifestation of our thoughts and feelings. The interconnectedness of all things: This theory posits that everything in the universe is connected, and that synchronicities are a sign of this underlying unity. The power of coincidence: This theory holds that synchronicities are simply coincidences that have been given meaning by our interpretation of them. Divine intervention: This theory suggests that synchronicities are a sign of some higher power at work in the universe. :: When we experience a synchronicity, it’s as if the universe is trying to communicate with us. These meaningful coincidences often occur when we’re going through a tough time or seeking answers to important questions. Some believe that synchronicities are messages from our higher selves, or even from otherworldly beings. Whether you subscribe to this belief or not, there’s no denying that these occurrences can be powerful and life-changing. Here are some more examples of synchronicity: You keep seeing the same number sequence everywhere you go, you meet someone randomly and they turn out to be connected to you in some way, you have a strong feeling that you’re supposed to do something, and then events begin to unfold that support your decision, If you’re open to it, synchronicity can provide valuable insights into the world beyond language and the entities that inhabit it.###\nwrite a conclusion paragraph for the following blog post about {title}: {post} ::",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=1,
      presence_penalty=.25,
      stop=["###"]
    )

    return response["choices"][0]["text"]