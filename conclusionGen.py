from apiKey import api
import openai

openai.api_key = (api)

def conclusionGen(title, subtitle):
    with open(title + ".html", "r") as post:
        post = post.read()
        post = post.replace("\n", " ")

    response = openai.Completion.create(
model="text-davinci-002",
prompt=f'write a conclusion paragraph for a blog post titled "The Power of Psychedelics : and how they can help us understand the nature of reality"-->Psychedelics have been used for centuries by indigenous people for healing and spiritual purposes. In recent years, there has been a resurgence of interest in these powerful substances, as more and more people are beginning to understand their potential. Psychedelics can help us to understand the nature of reality, and how our minds work. They can also be used to treat mental health conditions such as depression and anxiety. While psychedelics are not for everyone, they can be a powerful tool for personal growth and transformation.###\nwrite a conclusion paragraph for a blog post titled "How to Worship a Deity : What is Bhakti Yoga?"-->Bhakti yoga is the practice of devotion and worship of a deity. It is one of the most popular forms of yoga in India, and its popularity is growing in other parts of the world as well. Bhakti yoga can be practiced by anyone, regardless of their religious beliefs. The goal of Bhakti yoga is to develop a personal relationship with a chosen deity through prayer, chanting, and other devotional practices. Bhakti yoga is often practiced with the help of a guru, or teacher. This type of yoga can be very helpful for those who are seeking to connect with their spirituality and develop a deeper relationship with their chosen deity.###\nwrite a conclusion paragraph for a blog post titled "What are Sigils? : How are they used in chaos magic?"-->Sigils are powerful symbols that can be used for a variety of purposes, from manifesting your desires to protecting yourself from negative energy. While they are often associated with chaos magic, sigils can be used by anyone who believes in their power. If you’re open to using sigils in your life, pay attention to the signs and see what message they might be trying to tell you!###\nwrite a conclusion paragraph for a blog post titled "{title} : {subtitle}"-->',
temperature=0.9,
max_tokens=250,
top_p=1,
frequency_penalty=1,
presence_penalty=.8,
stop=["###", "-->"]
    )

    return response["choices"][0]["text"]
