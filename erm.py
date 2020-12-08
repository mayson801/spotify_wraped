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

    energy.append(get_average_playlist(anylised_playlist_2020, serchterms[1]))
    energy.append(get_average_playlist(anylised_playlist_2019, serchterms[1]))
    energy.append(get_average_playlist(anylised_playlist_2018, serchterms[1]))
    energy.append(get_average_playlist(anylised_playlist_2017, serchterms[1]))
    energy.append(get_average_playlist(anylised_playlist_2016, serchterms[1]))

    acousticness.append(get_average_playlist(anylised_playlist_2020, serchterms[2]))
    acousticness.append(get_average_playlist(anylised_playlist_2019, serchterms[2]))
    acousticness.append(get_average_playlist(anylised_playlist_2018, serchterms[2]))
    acousticness.append(get_average_playlist(anylised_playlist_2017, serchterms[2]))
    acousticness.append(get_average_playlist(anylised_playlist_2016, serchterms[2]))

    valence.append(get_average_playlist(anylised_playlist_2020, serchterms[3]))
    valence.append(get_average_playlist(anylised_playlist_2019, serchterms[3]))
    valence.append(get_average_playlist(anylised_playlist_2018, serchterms[3]))
    valence.append(get_average_playlist(anylised_playlist_2017, serchterms[3]))
    valence.append(get_average_playlist(anylised_playlist_2016, serchterms[3]))

    tempo.append(get_average_playlist(anylised_playlist_2020, serchterms[4]))
    tempo.append(get_average_playlist(anylised_playlist_2019, serchterms[4]))
    tempo.append(get_average_playlist(anylised_playlist_2018, serchterms[4]))
    tempo.append(get_average_playlist(anylised_playlist_2017, serchterms[4]))
    tempo.append(get_average_playlist(anylised_playlist_2016, serchterms[4]))

    duration_ms.append(get_average_playlist(anylised_playlist_2020, serchterms[5]))
    duration_ms.append(get_average_playlist(anylised_playlist_2019, serchterms[5]))
    duration_ms.append(get_average_playlist(anylised_playlist_2018, serchterms[5]))
    duration_ms.append(get_average_playlist(anylised_playlist_2017, serchterms[5]))
    duration_ms.append(get_average_playlist(anylised_playlist_2016, serchterms[5]))
    dataobject = {
        "dancibilty": danceablity,
        "energy": energy,
        "acousticness": acousticness,
        "valence": valence,
        "tempo": tempo,
        "duration_ms": duration_ms
    }
    return dataobject
def get_test():

    test=[[0.6510400000000002, 0.68268, 0.6317200000000002, 0.7155900000000002, 0.6788585858585859], [0.551642, 0.6296400000000001, 0.6332500000000001, 0.6459600000000001, 0.609909090909091], [0.32581963999999997, 0.20435314, 0.2318262059999999, 0.20808452999999996, 0.2023998181818182], [0.4423729999999999, 0.519387, 0.41333699999999995, 0.4749539999999998, 0.42940808080808085], [121.75788, 118.52533, 122.77667999999998, 119.67234000000003, 120.88778787878788], [214421.21, 243270.08, 220551.98, 219328.76, 235615.8686868687]]

    dataobject = {
        "dancibilty": test[0],
        "energy": test[1],
        "acousticness": test[2],
        "valence": test[3],
        "tempo": test[4],
        "duration_ms": test[5]
    }
    return dataobject

testing = get_test()
print(testing)












