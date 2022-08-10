from titleGen import titleGen
from introGen import introGen
from quoteGen import quoteGen
from bodyOutlineGen import BOGen
from bodyParagraphGen import BPGen
from conclusionGen import conclusionGen
import os

while True:
    done = False
    titleChoice = input("\n(C)ustom title, or (A)uto-title? ")

    if titleChoice.lower() == "c":
        title = input("(B for back) Title: ")
        break
    while True:
        if titleChoice.lower() == "a":
            print("\n\nGenerating title...")
            title = titleGen()
            titleSelect = input("\n\"" + title + "\"\n\nY or N? (or B for back) ")
            if titleSelect.lower() == "y":
                done = True
                break
            elif titleSelect.lower() == "b":
                break
    if done:
        break

os.chdir("posts")

with open(title, 'x') as post:
    # Title
    post.write("Title:\n" + title + "\n\n")

    # Credit to albert.py
    post.write("The following was written by an AI\n\n")

    # Quote
    print("Generating quote...")
    post.write("Quote:\n" + quoteGen(title) + "\n\n")

    # Intro
    print("Generating introduction...")
    post.write("Introduction:\n" + introGen(title) + "\n\n")

    # Body
    print("Generating body...")
    for part in BOGen(title).split("\n"):
        if part:
            post.write(part + "\n" + BPGen(title, part) + "\n\n")

    # Conclusion
    print("Generating conclusion...")
    post.write("Conclusion:\n" + conclusionGen(title) + "\n\n")


print("printed to posts folder")
