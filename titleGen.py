from apiKey import api
import openai
import os
import datetime
from clear import clear

openai.api_key = (api)

# Make a new directory
# make a list of the folder names in posts folder
scriptDir = os.path.dirname(__file__)
postsDir =  os.path.join(scriptDir, "posts")

folderList = os.listdir(postsDir)
dateList = []
for folder in folderList:
    # make a list of the dates taken from the folder names
    folder = folder.replace("week of ", "")
    dateList.append(folder)
# get the latest date from the list of dates
latestDate = sorted(dateList, key = lambda d: datetime.datetime.strptime(d, "%B %d %Y"), reverse=True)[0]
# add seven days to the date
latestDate = datetime.datetime.strptime(latestDate, "%B %d %Y")
newFolderDate = latestDate + datetime.timedelta(days = 7)

dir = postsDir + "/week of " + newFolderDate.strftime("%B %d %Y")



def titlePicker():
    weeklyTitles = []

    # clear soft title logs in main folder
    os.chdir(scriptDir)
    open("softTitleLog", "w").close()
    open("rejectedTitles", "w").close()



    # generate 7 starting titles
    print("Generating Titles...")
    ii = 1
    while ii <= 7:
        # generate title, delete any empty lines
        title = titleGen()

        title = title.replace("\n", "")

        # add title to soft title log
        os.chdir(scriptDir)
        with open("softTitleLog", "a") as log:
            log.write(title + "\n")

        # add title to list of accepted titles
        weeklyTitles.append(title)

        ii += 1



    while True:
        clear()
        # print list of titles
        for x in weeklyTitles:
            print(f"{weeklyTitles.index(x) + 1}) {x}")
        try:
            print("\nweekly titles:" + weeklyTitles + "\n" + editChoice)
        except Exception: pass


        # title creation menu
        titleChoice = input(f"\n\n(E)dit a title, or (D)one?\n\t>>> ")


        # edit a title
        if titleChoice == "e":
            editChoice = int(input("Which title would you like to edit? (input a number): ")) - 1


            while True:
                if editChoice <= len(weeklyTitles):
                    editType = input("\n(C)ustom title, or (A)uto-title?\n\t>>> ")

                # custom title
                if editType.lower() == "c":
                    title = input("(B for back) Title: ")

                    # B for back
                    if title.lower() == "b":
                        break

                    # if not B for back:
                    else:
                        # add title to soft title log
                        os.chdir(scriptDir)
                        with open("softTitleLog", "a") as log:
                            log.write(title + "\n")
                        # add title to list of accepted titles
                        weeklyTitles[editChoice] = title
                        break

                # auto tile
                elif editType.lower() == "a":
                    print("\n\nGenerating title...")
                    # generate tile, delete any empty lines
                    title = titleGen()
                    title = title.replace("\n", "")
                    # prompt user to accept or reject title
                    titleSelect = input(f"\n\"{title}\"\n\nReplace title {editChoice + 1} with this title? (Y)es, (N)o, or (B)ack\n\t>>> ")

                    # if title is accepted:
                    if titleSelect.lower() == "y":
                        # add title to soft title log
                        os.chdir(scriptDir)
                        with open("softTitleLog", "a") as log:
                            log.write(title + "\n")
                        # replace rejected title with new title in list of accepted titles
                        weeklyTitles[editChoice] = title

                        print(weeklyTitles)
                        break

                    # if title is rejected:
                    elif titleSelect.lower() == "n":
                        # add title to list of rejected titles
                        os.chdir(scriptDir)
                        with open("rejectedTitles", "a") as log:
                            log.write(title + "\n")
                        continue

                    # B for back
                    elif titleSelect.lower() == "b":
                        break


            else:
                break

        # done
        elif titleChoice.lower() == "d":
            # Make a new directory
            os.mkdir(dir)

            # write titles to title log
            os.chdir(scriptDir)
            for x in weeklyTitles:
                with open("titleLog", "a") as log:
                    log.write(x + "\n")

            return weeklyTitles





def titleGen():

    os.chdir(scriptDir)
    # get hard titles
    with open("titleLog", "r") as log:
        titles = log.read().replace("\n", ", ")

    # get soft titles
    with open("softTitleLog", "r") as softLog:
        softTitles = softLog.read().replace("\n", ", ")

    # get soft rejected titles
    with open("rejectedTitles", "r") as rejected:
        rejectedTitles = rejected.read().replace("\n", ", ")

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"This is a list of suitable titles for a blog about spirituality:\n{titles}, {softTitles}\n\n This is a list of unsuitable titles:\n{rejectedTitles}\n\nWrite one more unique and engaging title, to add to the list of suitable titles and subtitles, without repeating anything from that list.",
      temperature=.9,
      max_tokens=256,
      top_p=1,
      frequency_penalty=1.6,
      presence_penalty=.6,
      stop=["###"]
    )

    title = response["choices"][0]["text"]

    return title

def subtitleGen(title):

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"Create a subtitle for this title - True Hallucinations by Terrance McKenna:A book review (written by an AI)###\nCreate a subtitle for this title - The Secret Language of Symbols:and how they can help us understand the world around us###Create a subtitle for this title - {title}:",
      temperature=.9,
      max_tokens=256,
      top_p=1,
      frequency_penalty=1,
      presence_penalty=.6,
      stop=["###"]
    )

    subtitle = response["choices"][0]["text"]
    return(subtitle)
