
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import re
import pandas as pd
import numpy as np
app = Flask(__name__)
Data = pd.read_csv("DataL2.csv")
Data = Data.dropna()

MainImage = Data['MainImage']
Title = Data['Title']
DataFilter = Data['DataFilter']
Subtitle = Data['Subtitle']
DramaPlace = Data['DramaPlace']
Dialogue = Data['Dialogue']
Place = Data['Place']
Address = Data['Address']
LatitudeValue = Data['LatitudeValue']
LongitudeValue = Data['LongitudeValue']
SubImage = Data["SubImage"]


@app.route("/", methods=['GET', 'POST'])
def drama_place():
    return render_template("10PJ.html",DramaPlace=DramaPlace,DataFilter=DataFilter,LatitudeValue=LatitudeValue,
    LongitudeValue=LongitudeValue,Dialogue=Dialogue,Place=Place,Address=Address,Title=Title,Subtitle=Subtitle,MainImage=MainImage,
    len=len(Data))

@app.route('/locatesingle03', methods=['GET', 'POST'])
def locatesingle03():
    InputPlace = request.args.get('Place')
    IDX = np.where(Place == InputPlace)[0]

    return render_template(
        'locatesingle03.html',
        DramaPlace=DramaPlace[IDX].values[0],
        DataFilter=DataFilter[IDX],
        LatitudeValue=list(Data["LatitudeValue"][IDX].values),
        LongitudeValue=LongitudeValue[IDX].values,
        Dialogue=Dialogue[IDX].values[0],
        Place=Place[IDX].values[0],
        Address=Address[IDX].values[0],
        Title=Title[IDX],
        Subtitle=Subtitle[IDX],
        MainImage=MainImage[IDX],
        SubImage=SubImage[IDX]
        )

app.run(host='localhost', port='5000')
