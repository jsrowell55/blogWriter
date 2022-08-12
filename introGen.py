from apiKey import api
from titleGen import titleGen
import openai

openai.api_key = (api)

def introGen(title, subtitle):
    with open(title + ".html", "r") as post:
        post = post.read()
        post = post.replace("\n", " ")

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"Create an introduction paragraph to a blog post titled What is Synchronicity? : and how can it teach us about the world outside our minds?:What is Synchronicity? : and how can it teach us about the world outside our minds? :: The following was written by an AI “In synchronicity we are recognizing our own nature” -Deepak Chopra -->There’s something both mysterious and magical about synchronicity. It’s as if the universe is conspiring to send us a message. Whether it’s a chance meeting with a stranger or a series of events that seem to be connected, synchronicity often leaves us feeling amazed and bewildered. While the concept of synchronicity is often associated with positive experiences, it can also occur during difficult times. For example, you might suddenly find yourself thinking about someone you haven’t seen in years right before they walk into the room. Or you might have a dream about an upcoming event that later comes true. Synchronicity can be interpreted in many different ways, but one thing is certain: it’s a reminder that we’re all connected in ways we may not always be able to understand.###\nCreate an introduction paragraph to a blog post titled True Hallucinations by Terrance McKenna : A book review :: The following was written by an AI “True Hallucinations is one of the most mind-bending, reality-twisting books I’ve ever read. It’s a wild ride through the looking glass into a world where time and space seem to break down and the impossible becomes reality. If you’re looking for a book that will challenge your perceptions and leave you questioning everything you thought you knew, True Hallucinations is a must-read.”— Michele Wucker, author of The Gray Rhino -->True Hallucinations is a book about Terrance McKenna’s experience with psychedelics. He explores the mystical and spiritual aspects of these drugs, and how they can alter our perception of reality. While McKenna’s writing can be dense at times, it is also full of insights and stories that are both fascinating and enlightening. If you’re interested in psychedelics and their potential to change our consciousness, then True Hallucinations is definitely worth a read.###\nCreate an introduction paragraph to a blog post titled The Art of Letting Go : How to live in the present moment and let go of your past :: The following was written by an AI \"The art of letting go is one of the most difficult things to learn in life. It's hard to let go of things we've been holding onto for so long. But sometimes, we need to let go in order to move on.\" -Unknown -->Do you find yourself dwelling on past experiences or worrying about the future? If so, you\'re not alone. It's easy to get caught up in our thoughts and forget to live in the present moment. But what if we could learn to let go of our past and focus on the present? The art of letting go is about more than just forgetting our troubles. It's about learning to live in the present moment and appreciate all that life has to offer. When we let go of our past, we open ourselves up to new experiences and new possibilities. If you're ready to let go of your past and live in the present, here are some tips to get you started: \nIdentify your triggers\nAcknowledge your feelings\nPractice self-compassion\nLet go of your need to control\nFind a support system\nMake a plan\nTake action\nBe patient\nReward yourself###\nCreate an introduction paragraph to a blog post titled {title} : {subtitle} :: {post} -->",
      temperature=0.9,
      max_tokens=300,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["###", "-->"]
    )

    return response["choices"][0]["text"]
