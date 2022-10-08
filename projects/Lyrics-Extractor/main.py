# importing modules
from lyrics_extractor import SongLyrics
 
# Create GCS_API_KEY & GCS_ENGINE_ID
GDC_API_KEY = 'AIzaSyC5VTPmhIyI4biGRfB07qWWg9fmuX11HzE'
GCS_ENGINE_ID = 'e23ba5438f21746db'

extract_lyrics = SongLyrics(GDC_API_KEY, GCS_ENGINE_ID)

query = input('Enter the song name:')
out = extract_lyrics.get_lyrics(query)
print(
    f"""
    Title: {out["title"]}\n
    Lyrics:\n
    {out["lyrics"]}
    """
)
