import os

path = os.getcwd()
for file in os.listdir(path):
    if file.endswith(".mp3"):
        print(file)