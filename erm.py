import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json


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

#get the track_anaylis for songs
def track_anaylis(auth,track_id):
    track_data = auth.audio_features(track_id)
    track_data = track_data[0]
    return track_data

#get the anaylis a whole playlist and returns anylised tracks
def playlist_anylised(auth,playlist_id,):
    playlist = search_playlist_for_tracks(auth, playlist_id)
    anaysied_playlist=[]
    for track in playlist:
        track_data = track_anaylis(auth, track,)
        anaysied_playlist.append(track_data)
    print(anaysied_playlist[0]['danceability'])
    return (anaysied_playlist)

#get the average based on track_anaylis_type
def get_average_playlist(anylised_playlist,track_anaylis_type):
    average = 0.0
    for track in anylised_playlist:
        average = average+track[track_anaylis_type]
    average=average/len(anylised_playlist)
    return average

def get_all_data():
    # playsits_ids has all the "spotify wrapped" playlist in the order of: 2020,2019,2018,2017,2016
    playlist_ids = ['37i9dQZF1EMbHorF4q0hzh', '37i9dQZF1Etkg9uaN5u9lE', '37i9dQZF1EjqFmM8rDWrlv', '37i9dQZF1E9MVeJ7JZ0P05', '37i9dQZF1Cz0l6Re8lhihH']
    serchterms = ["danceability", "energy", "acousticness", "valence", "tempo", "duration_ms"]
    danceablity = []
    energy = []
    acousticness = []
    valence = []
    tempo = []
    duration_ms = []

    auth = log_in()

    anylised_playlist_2020 = playlist_anylised(auth, playlist_ids[0])
    anylised_playlist_2019 = playlist_anylised(auth, playlist_ids[1])
    anylised_playlist_2018 = playlist_anylised(auth, playlist_ids[2])
    anylised_playlist_2017 = playlist_anylised(auth, playlist_ids[3])
    anylised_playlist_2016 = playlist_anylised(auth, playlist_ids[4])

    danceablity.append(get_average_playlist(anylised_playlist_2020, serchterms[0]))
    danceablity.append(get_average_playlist(anylised_playlist_2019, serchterms[0]))
    danceablity.append(get_average_playlist(anylised_playlist_2018, serchterms[0]))
    danceablity.append(get_average_playlist(anylised_playlist_2017, serchterms[0]))
    danceablity.append(get_average_playlist(anylised_playlist_2016, serchterms[0]))
    return (danceablity,energy,acousticness,valence,tempo,duration_ms)
def get_test():

    test=[[0.6510400000000002, 0.68268, 0.6317200000000002, 0.7155900000000002, 0.6788585858585859], [], [], [], [], []]
    dataobject = {
        "dancibilty": test[0],
        "energy": test[1],
        "acousticness": test[2],
        "valence": test[3],
        "tempo": test[4],
        "duration_ms": test[5]
    }
    json_data = json.dumps(dataobject)
    return dataobject

testing = get_test()
print(testing)












