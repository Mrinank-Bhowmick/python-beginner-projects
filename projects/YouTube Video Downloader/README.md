# YouTube Video Downloader

A console tool that downloads a YouTube video using `yt-dlp`. It lists the available formats and lets you pick one or auto-selects the highest resolution.

## Example

```text
Enter the URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
140:    webm (144p)
160:    mp4 (144p)
18:     mp4 (360p)
22:     mp4 (720p)
Do you want to select from the available options? (y/n): y
Enter the format id of the video: 22
[download] Rick Astley - Never Gonna Give You Up.mp4 100% ...
Download complete using yt-dlp!
```

The video is saved in the current directory using the title as the filename.

## How to run on localhost

```bash
pip install yt-dlp
python you_tube_analyzer.py
```

## Dependencies

- yt-dlp
