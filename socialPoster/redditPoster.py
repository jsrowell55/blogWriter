from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep


def reddit(driver, title, url, subreddits):

    redditUsername = input("What is your reddit username?")
    redditPassword = input("What is your reddit password?")

    # open reddit login page -----------------------------
    driver.get("https://www.reddit.com/login")


    # Login to Reddit

    # send username to username box
    idBox = driver.find_element("id","loginUsername").send_keys(redditUsername)

    # send password to password box and press enter
    passBox = driver.find_element("id","loginPassword").send_keys(redditPassword + Keys.RETURN)

    # wait for login
    WebDriverWait(driver, 10).until(lambda driver: driver.current_url == "https://www.reddit.com/")


    # Post to subreddits

    print(subreddits)
    for sub in subreddits:

        # wait 1 second
        sleep(1)

        # check blacklist
        with open("subredditBlacklist", "r") as blacklist:
            blackSubreddits = blacklist.read().split("\n")
            for x in blackSubreddits:
                x = x.replace("\n", "")
                x = x.replace(" ", "")
            blackSubreddits.pop(len(blackSubreddits) - 1)
            if sub.lower() in blackSubreddits:
                print(f"failed posting to {sub} : blacklisted subreddit")
                continue


        # go to subreddit link post prompt
        try:
            driver.get(f"https://www.reddit.com/r/{sub}/submit?url=")
        except:
            print(f"failed posting to {sub} : invalid subreddit")
            continue


        # wait for post prompt
        try:
            WebDriverWait(driver, 5).until(lambda driver: driver.current_url == f"https://www.reddit.com/r/{sub}/submit?url=")
        except:
            print(f"failed posting to {sub} : not allowed to post here")
            continue


        # send url to url box
        try:
            driver.find_element("id", "url").send_keys(url)
        except:
            print(f"failed posting to {sub} : subreddit does not allow link submission")
            continue


        # send title to title box
        try:
            driver.find_element("name", "title").send_keys(f"An AI wrote this blog post: {title}")
        except:
            print(f"failed posting to {sub} : couldn't find title box")
            continue

        # display all flairs
        try:
            driver.find_element("xpath", "//*[@id='flair-field']/div/div/button").click()
            input("Press enter when you've chosen a flair")
        except:
            pass

        # click submit button
        try:
            driver.find_element("name", "submit").click()
        except:
            print(f"failed posting to {sub} : couldn't find submit button")
            continue

        print(f"posted to {sub}")
