import pickle
import numpy as np
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        model = pickle.load(open('app/admissions_rf.pkl', 'rb'))
        scaler_X = pickle.load(open('app/scaler_X.pkl', 'rb'))
        scaler_y = pickle.load(open('app/scaler_y.pkl', 'rb'))
        
        data = request.get_json()  # Get data posted as a json
        data = np.array(data)[np.newaxis, :]  # converts shape from (7,) to (1, 7)
        data = scaler_X.transform(data) # scale the input
        pred = model.predict(data)  # runs globally loaded model on the data
        pred = scaler_y.inverse_transform(pred) # descale the output
        pred = 100*pred
    return "You have a "+str(int(pred[0]))+"% chance of getting admitted!"