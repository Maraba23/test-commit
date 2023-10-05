import os
import sys
import time

def main():

    commits = input("How many commits do you want to make? ")

    #check readme.md
    if not os.path.exists("readme.md"):
        print("readme.md not found")
        return
    #check if git is installed
    if os.system("git --version") != 0:
        print("git not found")
        return
    '''
    Add this text to readme.md

    Commiter bot by Maraba23
    '''

    #add text to readme.md
    os.system("echo Commiter bot by Maraba23 >> readme.md")
    #commit and push
    os.system("git add .")
    os.system("git commit -m \"Added text to readme.md\"")
    os.system("git push -u origin master")

    #loop (delete the text, then add it again)
    for i in range(commits):
        #delete text
        os.system("sed -i '$ d' readme.md")
        #commit and push
        os.system("git add .")
        os.system("git commit -m \"Deleted text from readme.md\"")
        os.system("git push -u origin master")
        #wait 30 seconds
        time.sleep(30)
        #add text
        os.system("echo Commiter bot by Maraba23 >> readme.md")
        #commit and push
        os.system("git add .")
        os.system("git commit -m \"Added text to readme.md\"")
        os.system("git push -u origin master")

if __name__ == "__main__":
    main()