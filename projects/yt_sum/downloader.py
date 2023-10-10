import yt_dlp as ydlp

def download_audio(youtube_url, output_folder='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_folder}/audio',
    }

    with ydlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=1aA1WGON49E"
    download_audio(url)
