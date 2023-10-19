from typing import Tuple, List
import implicit
import scipy
from data import load_user_songs, SongRetriever

class ImplicitRecommender:
    def __init__(
        self,
        song_retriever: SongRetriever,
        implicit_model: implicit.recommender_base.RecommenderBase,
    ):
        self.song_retriever = song_retriever
        self.implicit_model = implicit_model
    def fit(self, user_songs_matrix: scipy.sparse.csr_matrix) -> None:
        self.implicit_model.fit(user_songs_matrix)
    def recommend(
        self,
        user_id: int,
        user_songs_matrix: scipy.sparse.csr_matrix,
        n: int = 10,
    ) -> Tuple[List[str], List[float]]:
        song_ids, scores = self.implicit_model.recommend(
            user_id, user_songs_matrix[n], N=n
        )
        songs = [
            self.song_retriever.get_song_name_from_id(song_id)
            for song_id in song_ids
        ]
        return songs, scores

if __name__ == "__main__":
    user_songs = load_user_songs("data.csv")
    song_retriever = SongRetriever()
    song_retriever.load_songs()
    implict_model = implicit.als.AlternatingLeastSquares(
        factors=50, iterations=10, regularization=0.01
    )
    recommender = ImplicitRecommender(song_retriever, implict_model)
    recommender.fit(user_songs)
    songs, scores = recommender.recommend(54, user_songs, n=5)
    for song, score in zip(songs, scores):
        print(f"{song}")