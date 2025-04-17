from yt_dlp import YoutubeDL
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import re

client_id="YOUR_CLIENT_ID"
client_secret="YOUR_CLIENT_SECRET"



def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()

print("\nDo you want to download from Spotify or Youtube?")
ChoiceOfService = int(input("\nSpotify(1) - Youtube(2) - Exit(0)"))


if ChoiceOfService == 1:
    print("\nDo you wish to download a playlist or an album?")
    ChoiceOfTask = int(input("\nPlaylist (1) - Album (2) - Exit (0) : "))

    if ChoiceOfTask == 1: 

        scope = "playlist-read-private"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="http://127.0.0.1:8888/callback",
            scope=scope
        ))

        playlists = sp.current_user_playlists()
        playlist_list = []

        print("Your playlists:")
        for idx, playlist in enumerate(playlists['items']):
            playlist_list.append({
                'name':playlist['name'],
                'id': playlist['id'],
                'track_count':playlist['tracks']['total']
            })
            print(f"{idx}. {playlist['name']} - {playlist['tracks']['total']} tracks")

        selected_index = int(input("\nEnter the number of the playlist: "))

        if 0 <= selected_index < len(playlist_list):
            selected_playlist = playlist_list[selected_index]
            print(f"\nFetching Songs from playlist: {selected_playlist['name']}...\n")
            playlist_tracks = sp.playlist_tracks(selected_playlist['id'])

            tracks = []
            for idx, item in enumerate(playlist_tracks['items']):
                track = item['track']
                if track:
                    track_name = track['name']
                    artist_names = ', '.join([artist['name'] for artist in track ['artists']])
                    print(f"{idx}. {track_name} by {artist_names}")
                    tracks.append({'name': track_name, 'artists': artist_names})
        else:
            print("Invalid selection!")
            exit()


        playlist_folder = sanitize_filename(selected_playlist['name'])

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'320',
            }],
            'outtmpl': f'{playlist_folder}/%(title)s.%(ext)s',
            'paths': {'home': os.path.expanduser('~/Downloads')},
            'quiet': False,
            'noplaylist': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            for track in tracks:
                try:
                    search_query =f"ytsearch:{track['name']} {track['artists']}"
                    print(f"\nSearching for: {track['name']} {track['artists']}...")

                    ydl.download([search_query])
                    print(f"Downloaded: {track['name']}")
                except Exception as e:
                    print(f"Error downloading {track['name']}: {str(e)}")


    elif ChoiceOfTask == 2:
        scope = "user-library-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="http://127.0.0.1:8888/callback",
            scope=scope
        ))

        album_link = str(input("\nPlease put in the album link: "))
        album_tracks = sp.album_tracks(album_link)
        album_name = sp.album(album_link)

        print("\nTracks in the album:")
        tracks = []
        for idx, item in enumerate(album_tracks['items']):
            track = item
            track_name = track['name']
            artist_names = ', '.join([artist['name'] for artist in track ['artists']])
            print(f"{idx}. {track_name} by {artist_names}")
            tracks.append({'name': track_name, 'artists': artist_names})

        album_folder = sanitize_filename(album_name['name'])

        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'320',
        }],
        'outtmpl': f'{album_folder}/%(title)s.%(ext)s',
        'paths': {'home': os.path.expanduser('~/Downloads')},
        'quiet': False,
        'noplaylist': True,
    }
        with YoutubeDL(ydl_opts) as ydl:
            for track in tracks:
                try:
                    search_query =f"ytsearch:{track['name']} {track['artists']}"
                    print(f"\nSearching for: {track['name']} {track['artists']}...")

                    ydl.download([search_query])
                    print(f"Downloaded: {track['name']}")
                except Exception as e:
                    print(f"Error downloading {track['name']}: {str(e)}")

    elif ChoiceOfTask == 0:
        exit()

if ChoiceOfService == 2:
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key':'FFmpegExtractAudio',
        'preferredcodec':'mp3',
        'preferredquality':'320',
    }],
    'paths': {'home': os.path.expanduser('~/Downloads')},
    'quiet': False,
}
    link = str(input("Input the youtube link:" ))
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)

        if 'entries' in info_dict:
            playlist_title = info_dict.get('title', 'Untitled Playlist')
            playlist_folder = sanitize_filename(playlist_title)

            ydl_opts['outtmpl'] = f'{playlist_folder}/%(title)s.%(ext)s'
        
        else:
            ydl_opts['outtmpl'] = os.path.expanduser('~Downloads/%(title)s.%(ext)s')

        with YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
    
    except Exception as e:
        print(f"An  error occured: {e}")


elif ChoiceOfService == 0:
    exit()