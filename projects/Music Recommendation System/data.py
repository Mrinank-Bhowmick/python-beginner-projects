from pathlib import Path
import scipy
import pandas as pd

def load_user_songs(user_songs_file: Path) -> scipy.sparse.csr_matrix:
    user_songs = pd.read_csv(user_songs_file)
    user_songs.set_index(["User ID", "Song ID"], inplace=True)
    coo = scipy.sparse.coo_matrix(
        (
            user_songs['Listen Count'].astype(float),
            (
                user_songs.index.get_level_values(0),
                user_songs.index.get_level_values(1),
            ),
        )
    )
    return coo.tocsr()

class SongRetriever:
    def __init__(self):
        self._songs_df = None
    def get_song_name_from_id(self, song_id: int) -> str:
        if self._songs_df is not None:
            return self._songs_df.loc[song_id, "Song Name"]
        else:
            return "Song ID not found"
    def load_songs(self) -> None:
        songs_df = pd.read_csv('data.csv')
        songs_df.set_index("Song ID", inplace=True)  
        self._songs_df = songs_df

if __name__ == "__main__":
    song_retriever = SongRetriever()
    song_retriever.load_songs()
