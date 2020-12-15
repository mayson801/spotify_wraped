import pandas as pd
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#logs in to spotify
def log_in():
    sp=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="519376b16ec24e008ddd1adf343596bc",
                                           client_secret="ae25727bef7a4044a6e71ff8b43a9a92",
                                           redirect_uri="http://127.0.0.1:5000/",
                                           scope="user-library-read"))
    return sp
#gets all the track ids from the playlist
def search_playlist_for_tracks(auth, playlis_id):
    playlist = auth.playlist(playlis_id)
    playlist_track_id_array = []
    for item in (playlist['tracks']['items']):
        track_id = item['track']['id']
        playlist_track_id_array.append(track_id)
    return playlist_track_id_array
#get the track_anaylis for songs and returns in python directories format
def track_anaylis(auth,track_id):
    track_data = auth.audio_features(track_id)
    track_data = track_data[0]
    return track_data
def create_data_frame(songs):
    df = pd.DataFrame(songs,columns= ["danceability",
        "energy",
        "key",
        "loudness",
        "mode",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "type",
        "id",
        "uri",
        "track_href",
        "analysis_url",
        "duration_ms",
        "time_signature",
        2020,
        2019,
        2018,
        2017,
        2016,
])
    df.set_index("id", inplace = True)
    return df
def check_for_repete(id,data_frame):
    if id in data_frame.index.tolist():
        return True
    else:
        return False
def playlist_anylised(auth,playlist_id,year,data_frame):
    anaysied_playlist_songs = []
    repeat_tracks = []

    playlist = search_playlist_for_tracks(auth, playlist_id,)
    for track in playlist:
        if year ==2020:
            repete = False
        else:
            repete = check_for_repete(track,data_frame)
        if repete == False:
            track_data = track_anaylis(auth, track)
            track_data[2020] = False
            track_data[2019] = False
            track_data[2018] = False
            track_data[2017] = False
            track_data[2016] = False

            track_data[year] = True

            anaysied_playlist_songs.append(track_data)

        else:
            repeat_tracks.append(track)
    return (anaysied_playlist_songs,repeat_tracks)
def get_playlist_ids(auth):
    year=2020
    playlist_ids = []
    while year != 2015:
        results = auth.search(q='"your top songs "'+ str(year), type='playlist')
        if results['playlists']['items'][0]['owner']['id'] == "spotify":
            playlist_ids.append(results['playlists']['items'][0]['id'])
        year=year-1

    return playlist_ids

def main(log):
    year = 2020
    songs_df = pd.DataFrame()
    playlist_ids = get_playlist_ids(log)

    for playlist_id in playlist_ids:
        #gets the playlist anaylised returns array
        playlist = playlist_anylised(log,playlist_id,year,songs_df)
        #creats new data frame and adds that to main data frame
        dataframe = create_data_frame(playlist[0])
        songs_df = pd.concat([dataframe,songs_df])
        for song in playlist[1]:
            songs_df.at[song,year] = True
        year = year-1
        print(year)
    result = songs_df.to_json(orient="records")
    json_file = json.loads(result)
    return json_file
#if __name__ == '__main__':
 #   main(log_in())
