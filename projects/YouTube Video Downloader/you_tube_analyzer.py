from importlib.resources import path
import pytube
from pytube import exceptions, Playlist, Channel, Search


dat = int(
    input(
        """Select The option:
1.Video   2.Playlist   3.Channel information   4.Search  :\n"""
    )
)


def Video():
    url = input("Enter the video url : ")
    try:
        yt = pytube.YouTube(url)
    except exceptions.VideoUnavailable:
        print("Video Unavailable")
    except exceptions.VideoPrivate:
        print("Video is Private")
    except exceptions.AgeRestrictedError:
        print("Video is age restricted")
    else:
        yt.streams.all()
        vid = list(enumerate(yt))
        for i in vid:
            print(i)
        strm = int(input("Enter the index of the stream : "))
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length)
        print("Rating of video: ", yt.rating)
        yt[strm].download()
    print("Video Downloaded successfully...")


def list():
    playlist_url = input("Entere the playlist url : ")
    playlist = Playlist(playlist_url)

    for video in playlist.videos:
        video.streams.get_highest_resolution().download()
    print("Playlist downloaded sucessfully..")


def channel():
    channel_link = input("Enter Channel Link : ")
    channel = Channel(channel_link)
    print("Channel ID : " + channel.channel_id)
    print("Channel Name : " + channel.channel_name)
    print("No. of videos in the channel : " + len(channel.video_urls))


def search():
    search_query = input("Enter Search Query : ")
    s = Search(search_query)
    for i in s.results:
        print(i)
        print("\n")
    print("Suggestions regarding the topic : \n")
    for j in s.completion_suggestions:
        print(j)


if dat == 1:
    Video()
elif dat == 2:
    list()
elif dat == 3:
    channel()
elif dat == 4:
    search()
