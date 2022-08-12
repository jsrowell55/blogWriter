from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

twitterUsername = "officialunspoke"
twitterPassword = "Judyeric2020!"


def twitter(driver, title, url):

    # open reddit login page -----------------------------
    driver.get("https://twitter.com/i/flow/login")



    # Login to Twitter

    # wait for login page
    WebDriverWait(driver, 10).until(lambda driver: driver.current_url == "https://twitter.com/i/flow/login")

    # send username to username box
    idBox = driver.find_element("name", "text")
    idBox.send_keys(twitterUsername)

    # send password to password box and press enter
    passBox = driver.find_element("id","loginPassword").send_keys(redditPassword + Keys.RETURN)



    # Post to subreddit 
    # wait for login
    WebDriverWait(driver, 10).until(lambda driver: driver.current_url == "https://www.reddit.com/")

    # go to subreddit link post prompt
    driver.get(f"https://www.reddit.com/r/{subreddit}/submit?url=")

    # wait for post prompt
    WebDriverWait(driver, 10).until(lambda driver: driver.current_url == f"https://www.reddit.com/r/{subreddit}/submit?url=")
    # select title box
    titleBox = driver.find_element("tag name", "textarea")
    # send title
    titleBox.send_keys(f"An AI wrote this blog post: {title}")
    # select url box
    titleBox.send_keys(Keys.TAB + url)

    # wait for 1.5 seconds
    time.sleep(1.5)

    # find post button and press enter
    titleBox.send_keys(Keys.TAB*6 + Keys.ENTER)