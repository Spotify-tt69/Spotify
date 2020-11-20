from joblib import load
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import numpy as np


df = pd.read_csv('herokuspotify.csv')

X = df.drop(['region', 'position', 'month','day','region.1',
              'artist','track_name', 'track_id'], axis=1)
s = StandardScaler()
X = s.fit_transform(X)
nn = NearestNeighbors(n_neighbors=10)
nn.fit(X)


# def render_10(song_title):
    
    # input_row = df[df['track_name'] == song_title].iloc[0] #need to remove duplicate songs
    # input_row = pd.DataFrame(input_row).T
    # input_row.columns = ['region', 'position', 'month', 'day', 'year', 'region.1', 'streams',
    #     'artist', 'track_name', 'track_id', 'duration_ms', 'time_signature',
    #     'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    #     'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
    #     ]
    # input_row = input_row.drop(['region', 'position', 'month','day','region.1',
    #             'artist','track_name', 'track_id'], axis=1)
    # input_row = s.transform(input_row)
    # arr = nn.kneighbors(input_row.reshape(1, -1))
    # index_value = arr[1][0][1:11]
    # songs_rec = df['track_name'].iloc[index_value] + " By: " + df['artist'].iloc[index_value]

    # return '\n'.join(str(songs_rec))

def render_10(song_title):
    tracks = df['track_name']  #####create seperate df with just track names
    list_of_tracks = tracks.to_list() ####make track names into list in order for 'if' statement to function properly
    if song_title in list_of_tracks:
        input_row = df[df['track_name'] == song_title].iloc[0] #need to remove duplicate songs
        input_row = pd.DataFrame(input_row).T
        input_row.columns = ['region', 'position', 'month', 'day', 'year', 'region.1', 'streams',
            'artist', 'track_name', 'track_id', 'duration_ms', 'time_signature',
            'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
        input_row = input_row.drop(['region', 'position', 'month','day','region.1',
                    'artist','track_name', 'track_id'], axis=1)
        input_row = s.transform(input_row)
        arr = nn.kneighbors(input_row.reshape(1, -1))
        index_value = arr[1][0]#[1]
        songs_list = df['track_name'].iloc[index_value] + " by " + df['artist'].iloc[index_value]
        songs_db = pd.DataFrame(data=songs_list).reset_index().drop('index', axis=1)
        songs_arr = songs_db.to_numpy()
        songs_rec = songs_arr.tolist()

        return str(songs_rec)
        
    else:
        return "Song Not in Database. Spelling/Spacing Common Issues"