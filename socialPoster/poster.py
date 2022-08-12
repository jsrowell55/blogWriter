from selenium import webdriver
from socialPoster.mediumGetter import medium
from socialPoster.redditPoster import reddit
from socialPoster.twitterPoster import twitter
import openai
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from apiKey import api



def socialPoster():

    url = input("\nWhat is the URL of the Medium blog post?\n\t>>> ")


    # add empty line before debug part
    print("\n")

    # using firefox to access web
    driver = webdriver.Chrome()

    # post medium post to reddit
    title = medium(driver, url)


    # Generate subreddit list
    openai.api_key = (api)
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"make a list of 15 subreddits to use to advertise a blog post titled \"The Development of Human Consciousness : The Evolution of Our understanding of the Universe and Ourselves\"philosophy, psychology, sociology, anthropology, history, religion, spiritual, newage, meditation, mindfulness, alternativemedicine, selfimprovement, spiritualawakening, enlightenment, soul nexus###make a list of 15 subreddits to use to advertise a blog post titled \"The Psychodynamics of the Hermetic Universe : How Our Thoughts Create Our Reality?\"metaphysics, newage, philosophy, religion, selfimprovement, spiritual, spiritualawakening, occult, witchcraft, pagan, tarot, astrology, numerology, runes, alternativemedicine###make a list of 15 subreddits to use to advertise a blog post titled \"The Power of Positive Thinking : How to use it in your daily life\"selfimprovement, positivepsychology, psychology, mentalhealth, lifehacks, tips, productivity, organization, declutter, wellness, alternativemedicine, fitness, weightloss, healthy, anxiety###make a list of 15 subreddits to use to advertise a blog post titled {title}",
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=1.5,
      presence_penalty=1,
      best_of=3,
      stop=["###"]
    )

    subreddits = response["choices"][0]["text"]
    subreddits = list(subreddits.split(", "))


    reddit(driver, title, url, subreddits)
    #twitter(driver, title, url)
