# Spotify Playlist Generator
![Current Version](https://img.shields.io/badge/version-1.0.7-green.svg)

Spotipy's full documentation is online at [Spotipy Documentation](http://spotipy.readthedocs.org/).

## Features:
1. Play a song via your terminal
- Enter a song name and it will start playing in your spotify application
2. Get recommended a song based off of user input
- Enter 3 songs and it will generate a song based off of your input
3. Get a generated playlist made off of an existing playlist
- Enter a playlist url and it will generate a brand new playlist with similar songs

<img width="509" alt="image" src="https://user-images.githubusercontent.com/106450097/210877746-35c683d3-00cc-4cfe-91c9-5b29f2a9611c.png">
<img width="1038" alt="Screen Shot 2023-01-05 at 12 52 46 PM" src="https://user-images.githubusercontent.com/106450097/210877856-1c095c39-55d7-449b-9045-c7c3b8cc38c0.png">

# Getting started:
## Create a user_secrets file
1. Create a `utils` folder
2. Add `user_secrets.py to` that folder
3. Enter the following code into that file
```py
username = "YOUR-USERNAME-ID"
clientID = "YOUR-CLIENT-ID"
clientSecret = "YOUR-CLIENT-SECRET"
redirectURI = "YOUR-REDIRECT-URI" 

banner = """Welcome, {}!
---------------------------------------
| 0 | Exit                            |
| 1 | Play a Song                     |
| 2 | Get a song recommendation       |
| 3 | Generate a new playlist         |
---------------------------------------"""
```

## How to get secrets:
A full set of examples can be found in the [online documentation](http://spotipy.readthedocs.org/) and in the [Spotipy examples directory](https://github.com/plamere/spotipy/tree/master/examples).

To get started, install spotipy and create an app on https://developers.spotify.com/.
Add your new ID and SECRET to your environment:

## Reporting issues:
If you find any bugs, leave a comment or a pull request
