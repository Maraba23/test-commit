import os
import sys
import time

def add_text_to_readme():
    with open("readme.md", "a") as file:
        file.write("Committer bot by Maraba23\n")

def delete_last_line_from_readme():
    with open("readme.md", "r") as file:
        lines = file.readlines()
    with open("readme.md", "w") as file:
        file.writelines(lines[:-1])

def main():
    commits = int(input("How many commits do you want to make? "))

    # Check readme.md
    if not os.path.exists("readme.md"):
        print("readme.md not found")
        return

    # Check if git is installed
    if os.system("git --version") != 0:
        print("git not found")
        return

    add_text_to_readme()

    # Commit and push
    os.system("git add .")
    os.system("git commit -m \"Added text to readme.md\"")
    os.system("git push")

    for i in range(commits):
        delete_last_line_from_readme()

        # Commit and push
        os.system("git add .")
        os.system("git commit -m \"Deleted text from readme.md\"")
        os.system("git push")
        time.sleep(30)

        add_text_to_readme()
        os.system("git add .")
        os.system("git commit -m \"Added text to readme.md\"")
        os.system("git push")

if __name__ == "__main__":
    main()
