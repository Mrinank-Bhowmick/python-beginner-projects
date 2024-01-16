import yt_dlp


def download_youtube_video(video_url):
    """Downloads a YouTube video using yt-dlp."""

    ydl_opts = {
        "outtmpl": "%(title)s.%(ext)s",  # Output filename template
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        formats = info_dict.get("formats", None)

        # Print all the available formats and ask the user to select
        for f in formats:
            print(f"{f['format_id']}:\t{f['ext']} ({f.get('format_note', None)}p)")

        resolution_choice = input(
            "Do you want to select from the available options? (y/n): "
        )

        if resolution_choice.lower() == "y":
            format_id = input("Enter the format id of the video: ")
            ydl_opts["format"] = format_id
        else:
            # Select the highest resolution format
            highest_resolution = max(formats, key=lambda x: x.get("height", 0))
            format_id = highest_resolution["format_id"]
            ydl_opts["format"] = format_id

        # Download the video
        ydl.download([video_url])
        print("Download complete using yt-dlp!")


if __name__ == "__main__":
    video_url = input("Enter the URL: ")
    download_youtube_video(video_url)
