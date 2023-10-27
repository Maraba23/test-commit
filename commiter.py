import os
import sys
import time
import string
import random

def add_text_to_readme():
    with open("readme.md", "a") as file:
        file.write("Committer bot by Maraba23\n")

def delete_last_line_from_readme():
    with open("readme.md", "r") as file:
        lines = file.readlines()
    with open("readme.md", "w") as file:
        file.writelines(lines[:-1])

def create_random_files_with_text():
    for i in range(10):
        with open("".join(random.choices(string.ascii_letters, k=10)) + ".txt", "w") as file:
            file.write("".join(random.choices(string.ascii_letters, k=10)))

def delete_random_files():
    # delete all txt files from the current directory
    for filename in os.listdir():
        if filename.endswith(".txt"):
            os.remove(filename)

def main():
    tempo_input = int(input("How many seconds do you want to wait before the first commit? "))
    tempo = tempo_input
    commits = int(input("How many commits do you want to make? "))

    if not os.path.exists("readme.md"):
        print("readme.md not found")
        return

    if os.system("git --version") != 0:
        print("git not found")
        return
    while(tempo > 0):
        print("Next commit in " + str(tempo) + " seconds")
        tempo -= 1
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        time.sleep(1)
    create_random_files_with_text()

    os.system("git add .")
    os.system("git commit -m \"Testing the bot\"")
    os.system("git push")

    for i in range(commits):
        tempo = tempo_input
        while(tempo > 0):
            print("Next commit in " + str(tempo) + " seconds")
            tempo -= 1
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            time.sleep(1)
        delete_random_files()

        os.system("git add .")
        os.system("git commit -m \"Deleted txt files\"")
        os.system("git push")
        tempo = tempo_input
        while(tempo > 0):
            print("Next commit in " + str(tempo) + " seconds")
            tempo -= 1
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            time.sleep(1)

        create_random_files_with_text()
        os.system("git add .")
        os.system("git commit -m \"Added txt files\"")
        os.system("git push")

if __name__ == "__main__":
    main()
