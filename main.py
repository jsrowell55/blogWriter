from titleGen import titleGen, subtitleGen, titlePicker, dir
from quoteGen import quoteGen
from introGen import introGen
from bodyOutlineGen import BOGen
from bodyParagraphGen import BPGen
from conclusionGen import conclusionGen
import os
from clear import clear
from socialPoster.poster import socialPoster



# Start Screen
while True:
    clear()
    print("\nWelcome to albert.py")
    menu = input("""
    1) Generate 7 blog posts

    2) Post a post to Reddit

        >>> """)

    if menu == "1":
        clear()
        # Write to post file
        weeklyTitles = titlePicker()
        i = 1
        for currentTitle in weeklyTitles:
            subtitle = subtitleGen(currentTitle)
            clear()
            print(f"Generating post {i}/7 - {currentTitle}...\n")

            os.chdir(dir)
            with open(currentTitle + ".html", 'x') as post:
                # Title
                post.write("<h3>" + currentTitle + "</h3>\n<h4>" + subtitle + "</h4>")

                # Credit to albert.py
                post.write("<p><i>The following was written by an AI</i></p>\n\n")

                # Quote
                print("Generating quote...")
                post.write("<br/>\n\n<blockquote class='graf graf--blockquote graf--startsWithDoubleQuote graf-after--p is-selected'>" + quoteGen(currentTitle, subtitle) + "</blockquote>\n\n<br/>\n\n")

                # Intro
                print("Generating introduction...")
                post.write("<p>" + introGen(currentTitle, subtitle) + "</p>\n\n<hr/>\n\n")

                # Body
                print("Generating body...")
                for part in BOGen(currentTitle, subtitle).split("\n"):
                    if part:
                        post.write("<h3>" + part + "</h3>\n\n<p>" + BPGen(currentTitle, subtitle, part) + "</p>\n\n")

                # Conclusion
                print("Generating conclusion...")
                post.write("<hr/>\n\n<p>" + conclusionGen(currentTitle, subtitle) + "</p>\n\n")

            i += 1


    elif menu == "2":

        # social poster (only Reddit rn)
        socialPoster()


clear()
print("Done!")
