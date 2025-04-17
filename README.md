⚠️This is simply a hobby project ⚠️

# Playlist-Downloader
A python CLI script for Spotipy and yt-dlp to automatically list all your spotify playlists and download them as MP3's from youtube.

## Table of Contents
- [Prerequisites](#Prerequisites)
- [Setup](#Setup)
- [Usage](#Usage)

## Prerequisites

- Python 3.13.3 or higher
- pip
- ffmpeg 2025-04-17 or newer
- Spotify for Developers: Client ID & Client Secret

## Setup

- Install all the requirements included in requirements.txt using pip.
```
python -m pip install -r requirements.txt
```
- Download [ffmpeg](https://ffmpeg.org/download.html) and add it to PATH

  #### Adding ffmpeg to PATH
  **Windows**
  - Download Zip file
  - Extract the folders from the Zip
  - Move extracted folder to ``C:``
  - Rename extracted folder to ``ffmpeg``
  - Search ``Edit the system environment variables`` in the Start Menu
  - Navigate to ``Advanced`` and ``Environment Variables``
  - Select ``PATH`` and press ``Edit``
  - Press ``New``
  - Add ``C:\ffmpeg\bin`` to the empty field and confirm with OK.
  - Run ``ffmpeg -version`` in CMD or Powershell to see if it is correctly added to PATH

- Insert the spotify Client ID and Client Secret into the script in the appropriate fields.

  <sub> **Spotify ID is not required for Youtube downloads** </sub>
    
  This requires you to go to [Spotify for Developer](https://developer.spotify.com) and log in.
  Nagivate to the Dashboard and create a new app. 
    - The App requires the following
      ##### Redirect URIs
      ``http://127.0.0.1:8888/callback``
      ##### API/SDK
      Check the Box for: ``Web API``
      
Inside of the app, you will find your Client ID and Client Secret, these need to be added to the script for the script to be able to authenticate the account and be able to access Spotify.
## Usage

Run the script, select the playlist you wish to download.
```
py /Path/To/Script/PlaylistDownloader.py
```

