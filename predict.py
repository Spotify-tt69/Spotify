from joblib import load



pipeline = load('************')

@app.callback(
    Output('prediction-content', 'children'),
    [Input('age', 'value'),
     Input('education', 'value'),
     Input('maritalstatus', 'value'),
     Input('occupation', 'value'),
     Input('race', 'value'),
     Input('nativecountry', 'value'),
     Input('over40hrs','value'),
     Input('incomeover50K','value')])
def predict(age, education, maritalstatus, occupation, race, nativecountry, over40hrs, incomeover50K):
    df = pd.DataFrame(
        columns=['age', 'workclass', 'education', 'education-num', 'marital-status',
       'occupation','race', 'native-country',
       'income_over_50K', 'over40hrs'], 
        data=[[age, 'Private',education,9, maritalstatus, occupation, race, nativecountry,int(incomeover50K),int(over40hrs)]]
    )
    #this was used within a def function with the df
    y_pred = pipeline.predict(df)[0]
    if y_pred: 
        gender='Female'
    else:
        gender='Male'
    print(pipeline.predict_proba(df))
    return f'Gender Prediction: {gender}'