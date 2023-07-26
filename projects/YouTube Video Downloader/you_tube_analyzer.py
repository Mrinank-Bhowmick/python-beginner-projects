# Import necessary classes from the pytube library
from pytube import YouTube, exceptions, Playlist, Channel, Search

# Prompt the user to select an option: Video, Playlist, Channel information, or Search
dat = int(
    input(
        """Select The option:
1. Video   2. Playlist   3. Channel information   4. Search  :\n"""
    )
)


# Function to handle downloading a single video
def Video():
    # Prompt the user to enter the URL of the video
    url = input("Enter the video URL: ")

    try:
        # Try to create a YouTube object for the provided URL
        yt = YouTube(url)
    except exceptions.VideoUnavailable:
        # If the video is unavailable or has been removed, catch the VideoUnavailable exception
        print("Video Unavailable")
    except exceptions.VideoPrivate:
        # If the video is private, catch the VideoPrivate exception
        print("Video is Private")
    except exceptions.AgeRestrictedError:
        # If the video is age-restricted, catch the AgeRestrictedError exception
        print("Video is age-restricted")
    else:
        # If no exception occurred, display available streams for the video
        streams = yt.streams.all()
        vid = list(enumerate(streams))
        for i in vid:
            print(i)
        # Prompt the user to select a stream by its index
        strm = int(input("Enter the index of the stream: "))
        # Display video information and download the selected stream
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length)
        print("Rating of video: ", yt.rating)
        streams[strm].download()
    # Notify the user that the video download process is complete
    print("Video Downloaded successfully...")


# Function to download a playlist
def download_playlist(playlist_url):
    # Create a Playlist object for the provided playlist URL
    playlist = Playlist(playlist_url)
    # Download each video in the playlist with the highest resolution available
    for video in playlist.videos:
        video.streams.get_highest_resolution().download()
    # Notify the user that the playlist download process is complete
    print("Playlist downloaded successfully..")


# Function to get information about a YouTube channel
def channel():
    # Prompt the user to enter the URL of the channel
    channel_link = input("Enter Channel Link: ")
    # Create a Channel object for the provided channel URL
    channel = Channel(channel_link)
    # Display basic information about the channel
    print("Channel ID: " + channel.channel_id)
    print("Channel Name: " + channel.channel_name)
    # Get the number of videos in the channel and display it
    print("No. of videos in the channel: " + str(len(channel.video_urls)))


# Function to perform a YouTube search and display results
def search():
    # Prompt the user to enter the search query
    search_query = input("Enter Search Query: ")
    # Create a Search object for the provided search query
    s = Search(search_query)
    # Display search results (video URLs)
    for i in s.results:
        print(i)
        print("\n")
    # Display search suggestions related to the topic
    print("Suggestions regarding the topic:\n")
    for j in s.completion_suggestions:
        print(j)


# Based on the user's input, execute the appropriate function
if dat == 1:
    Video()
elif dat == 2:
    # If the user selected option 2, prompt for a playlist URL and download it
    playlist_url = input("Enter the playlist URL: ")
    download_playlist(playlist_url)
elif dat == 3:
    # If the user selected option 3, get information about a YouTube channel
    channel()
elif dat == 4:
    # If the user selected option 4, perform a YouTube search and display results
    search()
