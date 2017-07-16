#!/usr/bin/env python

from neural import initNeuralNetwork
from neural import query
from flask import Flask, request
import base64

neuralNetwork = initNeuralNetwork.setUpAndGetNetwork()

app = Flask(__name__)
app.static_folder = ''

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/input', methods=['POST'])
def input():
    requestImage = request.form['img'][22:]
    decodedImage = base64.b64decode(requestImage)

    image = open("input.png", "wb")
    image.write(decodedImage)
    image.close()

    ouputFromNeuralNetwork = query.queryNetwork(neuralNetwork)

    return ouputFromNeuralNetwork

print('Running on 5000!')