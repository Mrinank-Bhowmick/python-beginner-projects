import pandas as pd
import random

# Generate random User IDs
user_ids = [random.randint(1, 101) for _ in range(100)]

# Sample list of real song names
df = pd.read_csv('songs.csv')
song_names = df["song"].tolist()

# Generate the dataset
data = []
for _ in range(1000):
    user_id = random.choice(user_ids)
    song = random.choice(song_names)
    song_id = random.randint(1, 100000)
    listen_count = random.randint(1, 100)
    data.append([user_id, song, song_id, listen_count])

# Create a DataFrame
df = pd.DataFrame(data, columns=['User ID', 'Song Name', 'Song ID', 'Listen Count'])
df.to_csv('data.csv')
# Display the first few rows of the dataset
print(df)
