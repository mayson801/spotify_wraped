import  spotipy_code
import pandas as pd
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import date
import json
import datetime

current_year = 2022

def dump_to_json(dictionary):
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("test_json.json", "w") as outfile:
        outfile.write(json_object)

def playlist_anylised_new(auth,playlist_id):
    playlist = search_playlist_for_tracks(auth, playlist_id)
    playlist_songs_len=len(playlist[0])
    playlist_artist_len=len(playlist[1])
    artistJSON=[]

    track_array = []
    track_subdata=[]
    artisit_id_array=[]
    for indx,track in enumerate(playlist[0]):
        track_array.append(track["id"])
        if indx % 100 ==0 or indx+1==playlist_songs_len:
            track_subdata += (auth.audio_features(track_array))
            track_array=[]
    for indx,track in enumerate(playlist[0]):
        track['subdata']=track_subdata[indx]

    for indx,artist in enumerate(playlist[1]):
        artisit_id_array.append(artist)
        if indx % 50 == 0 or indx+1==playlist_artist_len:
            artistJSON+=(auth.artists(artisit_id_array))['artists']
            artisit_id_array=[]
    years=[]
    for i in playlist_ids:
        years.append(i[1])
    return playlist[0],artistJSON,years

def get_playlist_ids(auth):
        playlistids = []
        results = auth.search(q='your top songs 20', type='playlist', limit=50)
        for playist in (results['playlists']['items']):
            if "Your Top Songs 20" in str(playist['name']) and str(playist['owner']['id']) == "spotify":
                playlistids.append([playist['id'], str(playist['name'])[-4:]])
        playlistids.sort(key=lambda x: x[1], reverse=True)
        return playlistids

def search_playlist_for_tracks(auth, playlis_id):
    i=0
    playlist_track_id_array = []
    artist_track_array= []
    while i !=len(playlis_id):
        playlist = auth.playlist(playlis_id[i][0])
        for item in (playlist['tracks']['items']):
                artist = []
                for y in item['track']['artists']:
                    artist_list=False
                    for z in artist_track_array:
                        if z == y['id']:
                            artist_list=True
                            pass
                    if artist_list==False:
                        artist_track_array.append(y['id'])
                    artist.append(y['id'])
                track_id = item['track']['id']
                track_name = (item['track']['name'])
                albumb_art = (item['track']['album']['images'])
                release_date= (item['track']['album']['release_date'])
                in_track_list=False
                for track in playlist_track_id_array:
                    if track_id == track['id']:
                        in_track_list=True
                        track["year_added"].append(playlis_id[i][1])
                        pass
                if in_track_list==False:
                    track_data = {
                        "id": track_id,
                        "artist":artist,
                        "track_name": track_name,
                        "year_added":[playlis_id[i][1]],
                        "images":albumb_art,
                        "release_date":release_date
                    }
                    playlist_track_id_array.append(track_data)
        i=i+1
    return playlist_track_id_array,artist_track_array

def merge_arrays(arrays):
    for indxtrack,track in enumerate(arrays[0]):
        for indxartist,artist in enumerate(track['artist']):
            for artist_check in arrays[1]:
                if artist==artist_check['id']:
                    arrays[0][indxtrack]['artist'][indxartist]=artist_check
    return arrays[0],arrays[2]

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(now)
    log=spotipy_code.log_in()
    playlist_ids=get_playlist_ids(log)
    testdata=merge_arrays(playlist_anylised_new(log,get_playlist_ids(log)))
    now = datetime.datetime.now()
    print(now)

    dump_to_json(testdata)


