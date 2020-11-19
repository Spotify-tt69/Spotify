from joblib import load
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler


# pipeline = load('nnPipeline.joblib2')
df = pd.read_csv('herokuspotify.csv')

X = df.drop(['region', 'position', 'month','day','region.1',
              'artist','track_name', 'track_id'], axis=1)
s = StandardScaler()
X = s.fit_transform(X)
nn = NearestNeighbors(n_neighbors=10)
nn.fit(X)


def render_10(song_title):
    
    input_row = df[df['track_name'] == song_title].iloc[0] #need to remove duplicate songs
    input_row = pd.DataFrame(input_row).T
    input_row.columns = ['region', 'position', 'month', 'day', 'year', 'region.1', 'streams',
        'artist', 'track_name', 'track_id', 'duration_ms', 'time_signature',
        'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
        'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
        ]
    input_row = input_row.drop(['region', 'position', 'month','day','region.1',
                'artist','track_name', 'track_id'], axis=1)
    input_row = s.transform(input_row)
    arr = nn.kneighbors(input_row.reshape(1, -1))
    index_value = arr[1][0][1:11]
    songs_rec = df['track_name'].iloc[index_value] + " By: " + df['artist'].iloc[index_value]
    return str(songs_rec)
    



# @app.route('/predict')
# async def predict(item: Item):
#     return render_10
    # song = render_10(track_id, df)
    # prediction = pipeline(song)
    # arr = prediction[1][0][1]
    # # """
    # #   # Make random baseline predictions for classification problem 🔮
    # #   """
    # # pred = searchfunc(user_input=item.symptoms)
    # # print(pred)
    # # conn = sqlite3.connect('data/cannabis.sqlite3')
    # # curs = conn.cursor()
    # # curs.execute(f"SELECT * FROM Cannabis WHERE strain_id == {pred[0][0]}")


    #this was used within a def function with the df
    # y_pred = nnPipeline.predict(df)[0]
    # if y_pred: 
    #     gender='Female'
    # else:
    #     gender='Male'
    # print(pipeline.predict_proba(df))
    # return f'Gender Prediction: {gender}'