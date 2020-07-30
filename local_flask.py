import pickle
import numpy as np
from flask import Flask, request

model = None
scaler_X = None
scaler_y = None
app = Flask(__name__)


def load_model_and_scalers():
    global model
    # model variable refers to the global variable
    with open('model/admissions_rf.pkl', 'rb') as f:
        model = pickle.load(f)
    global scaler_X
    with open('scalers/scaler_X.pkl', 'rb') as f:
        scaler_X = pickle.load(f)
    global scaler_y
    with open('scalers/scaler_y.pkl', 'rb') as f:
        scaler_y = pickle.load(f)


@app.route('/', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a json
        data = np.array(data)[np.newaxis, :]  # converts shape from (7,) to (1, 7)
        data = scaler_X.transform(data) # scale the input
        pred = model.predict(data)  # runs globally loaded model on the data
        pred = scaler_y.inverse_transform(pred) # descale the output
        pred = 100*pred
    return "You have a "+str(int(pred[0]))+"% chance of getting admitted!"


if __name__ == '__main__':
    load_model_and_scalers()  # load model at the beginning once only
    app.run(host='localhost', port=6969)