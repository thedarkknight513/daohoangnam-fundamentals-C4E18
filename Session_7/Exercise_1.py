from youtube_dl import YoutubeDL

print("""
A - download a single youtube video
B - download multiple youtube video
C - Download audio
D - Search & download the first video
E - Search & download the first audio
""")

loop = True
while loop:
    user_response = input("What do you want to do (A - E)").upper()
    if user_response == "A":
#   Download a single youtube video
        dl1 = YoutubeDL()
        dl1.download(["https://www.youtube.com/watch?v=JmcA9LIIXWw"])

    elif user_response == "B":
    # Download multiple youtube video
        dl2 = YoutubeDL()
        dl2.download(["https://www.youtube.com/watch?v=PWgvGjAhvIw", "https://www.youtube.com/watch?v=SDTZ7iX4vTQ"])

    elif user_response == "C":
    # Download audio
        option = {
            "format": "best audio/audio"
        }
        dl3 = YoutubeDL(option)
        dl3.download(["https://www.youtube.com/watch?v=bpOSxM0rNPM"])

    elif user_response == "D":
#    Search and download the first video
        options = {
            "default_search": "ytsearch",
            "max_downloads": 1
        }
        dl4 = YoutubeDL(options)
        dl4.download(["Come as you are"])

    elif user_response == "E":

    # Search and then download the first audio
        option = {
            "default_search": "ytsearch",
            "max_downloads": 1,
            "format": "bestaudio/audio"
        }
        dl = YoutubeDL(option)
        dl.download(["https://www.youtube.com/watch?v=YVkUvmDQ3HY"])

    else:
        print("@@")