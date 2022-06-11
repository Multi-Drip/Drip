from flask import Flask, request, render_template, redirect
from flask_cors import CORS
import re
import random
import pandas as pd
import numpy as np
import os

app = Flask(__name__, static_url_path="/static")
Data = pd.read_csv("DataL2.csv")
Data = Data.dropna()

CORS(app)

MainImage = Data['MainImage']
Title = Data['Title']
DataFilter = Data['DataFilter']
PlaceFilter = Data['PlaceFilter']
Subtitle = Data['Subtitle']
DramaPlace = Data['DramaPlace']
Dialogue = Data['Dialogue']
Place = Data['Place']
Address = Data['Address']
LatitudeValue = Data['LatitudeValue']
LongitudeValue = Data['LongitudeValue']
SubImage = Data['SubImage']

@app.route("/", methods=['GET','POST'])
def MainPage():
    return render_template('10PJ.html',
                            len = len(Place),
                            DataFilter = DataFilter,
                            Place = Place,
                            MainImage = MainImage,
                            Title = Title,
                            Subtitle = Subtitle)

@app.route("/locatesingle", methods=['GET', 'POST'])
def LocatePage():
    InputPlace = request.args.get('Place')
    IDX = np.where(Place == InputPlace)[0]
    #return redirect("http://localhost:5000/locatesingle/"+result)
    return render_template('locatesingle.html',
                            DramaPlace=DramaPlace[IDX].values[0],
                            DataFilter=DataFilter[IDX],
                            LatitudeValue=LatitudeValue[IDX].values[0],
                            LongitudeValue=LongitudeValue[IDX].values[0],
                            Dialogue=Dialogue[IDX].values[0],
                            Place=Place[IDX].values[0],
                            Address=Address[IDX].values[0],
                            SubImage=SubImage[IDX])

@app.route("/map", methods=['GET','POST'])
def AllMap():
    return render_template('map.html')

app.run(host='0.0.0.0', port='80')