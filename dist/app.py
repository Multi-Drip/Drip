from flask import Flask, request, render_template, redirect
from flask_cors import CORS
import re
import random
import pandas as pd
import numpy as np
import os
from flask import Markup

app = Flask(__name__, static_url_path="/static")
Data = pd.read_csv("DataL2.csv")
Data_eng = pd.read_csv("Data_eng.csv")
Data_jpn = pd.read_csv("Data_jpn.csv")
Data = Data.dropna()
Data_eng = Data_eng.dropna()
Data_jpn = Data_jpn.dropna()
#cwd = os.getcwd()
#files = os.listdir(cwd)

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

MainImage_eng = Data_eng['MainImage']
Title_eng = Data_eng['Title']
DataFilter_eng = Data_eng['DataFilter']
PlaceFilter_eng = Data_eng['PlaceFilter']
Subtitle_eng = Data_eng['Subtitle']
DramaPlace_eng = Data_eng['DramaPlace']
Dialogue_eng = Data_eng['Dialogue']
Place_eng = Data_eng['Place']
Address_eng = Data_eng['Address']
LatitudeValue_eng = Data_eng['LatitudeValue']
LongitudeValue_eng = Data_eng['LongitudeValue']
SubImage_eng = Data_eng['SubImage']

MainImage_jpn = Data_jpn['MainImage']
Title_jpn = Data_jpn['Title']
DataFilter_jpn = Data_jpn['DataFilter']
PlaceFilter_jpn = Data_jpn['PlaceFilter']
Subtitle_jpn = Data_jpn['Subtitle']
DramaPlace_jpn = Data_jpn['DramaPlace']
Dialogue_jpn = Data_jpn['Dialogue']
Place_jpn = Data_jpn['Place']
Address_jpn = Data_jpn['Address']
LatitudeValue_jpn = Data_jpn['LatitudeValue']
LongitudeValue_jpn = Data_jpn['LongitudeValue']
SubImage_jpn = Data_jpn['SubImage']


@app.route("/", methods=['GET', 'POST'])
def MainPage():
    return render_template('10PJ.html',
                           len=len(Place),
                           DataFilter=DataFilter,
                           Place=Place,
                           MainImage=MainImage,
                           Title=Title,
                           Subtitle=Subtitle)


@app.route("/engmain", methods=['GET', 'POST'])
def EngMain():
    return render_template('engmain.html',
                           len=len(Place_eng),
                           DataFilter_eng=DataFilter_eng,
                           Place_eng=Place_eng,
                           MainImage_eng=MainImage_eng,
                           Title_eng=Title_eng,
                           Subtitle_eng=Subtitle_eng)


@app.route("/jpnmain", methods=['GET', 'POST'])
def JpnMain():
    return render_template('jpnmain.html',
                           len=len(Place_jpn),
                           DataFilter_jpn=DataFilter_jpn,
                           Place_jpn=Place_jpn,
                           MainImage_jpn=MainImage_jpn,
                           Title_jpn=Title_jpn,
                           Subtitle_jpn=Subtitle_jpn)


@app.route("/about", methods=['GET', 'POST'])
def About():
    return render_template('about.html')


@app.route("/jpnabout", methods=['GET', 'POST'])
def JPNAbout():
    return render_template('jpnabout.html')


@app.route("/engabout", methods=['GET', 'POST'])
def ENGAbout():
    return render_template('engabout.html')


@app.route("/coursejj", methods=['GET', 'POST'])
def coursejj():
    return render_template('course01jj.html')


@app.route("/coursegj", methods=['GET', 'POST'])
def Coursegj():
    return render_template('course02gj.html')


Gw = pd.read_csv("gangwon_place.csv", encoding="cp949")
Gw = Gw.dropna()
GwFilter = Gw['filter']
GwName = Gw['name']
GwDistance = Gw['distance']
GwImg = Gw['img']
GwLink = Gw['link']
GwDetail = Gw['detail']          
@app.route("/coursegw", methods=['GET','POST'])
def Coursegw():
    return render_template('course03gw.html',
                           lengw = len(GwName),
                           GwFilter = GwFilter,
                           GwName = GwName,
                           GwDistance = GwDistance,
                           GwImg = GwImg,
                           GwLink = GwLink,
                           GwDetail = GwDetail)


@app.route("/coursesu", methods=['GET', 'POST'])
def Coursesu():
    return render_template('course04su.html')


@app.route("/locatesingle", methods=['GET', 'POST'])
def LocatePage():
    InputPlace = request.args.get('Place')
    IDX = np.where(Place == InputPlace)[0]
    return render_template('locatesingle.html',
                           DramaPlace=DramaPlace[IDX].values[0],
                           DataFilter=DataFilter[IDX],
                           LatitudeValue=LatitudeValue[IDX].values[0],
                           LongitudeValue=LongitudeValue[IDX].values[0],
                           Dialogue=Markup(Dialogue[IDX].values[0]),
                           Place=Place[IDX].values[0],
                           Address=Address[IDX].values[0],
                           SubImage=SubImage[IDX])


@app.route("/engsub", methods=['GET', 'POST'])
def EngSub():
    InputPlace_eng = request.args.get('Place')
    IDX = np.where(Place_eng == InputPlace_eng)[0]
    return render_template('engsub.html',
                           DramaPlace_eng=DramaPlace_eng[IDX].values[0],
                           DataFilter_eng=DataFilter_eng[IDX],
                           LatitudeValue_eng=LatitudeValue_eng[IDX].values[0],
                           LongitudeValue_eng=LongitudeValue_eng[IDX].values[0],
                           Dialogue_eng=Markup(Dialogue_eng[IDX].values[0]),
                           Place_eng=Place_eng[IDX].values[0],
                           Address_eng=Address_eng[IDX].values[0],
                           SubImage_eng=SubImage_eng[IDX])


@app.route("/jpngub", methods=['GET', 'POST'])
def JpnSub():
    InputPlace_jpn = request.args.get('Place')
    IDX = np.where(Place_jpn == InputPlace_jpn)[0]
    return render_template('jpnsub.html',
                           DramaPlace_jpn=DramaPlace_jpn[IDX].values[0],
                           DataFilter_jpn=DataFilter_jpn[IDX],
                           LatitudeValue_jpn=LatitudeValue_jpn[IDX].values[0],
                           LongitudeValue_jpn=LongitudeValue_jpn[IDX].values[0],
                           Dialogue_jpn=Markup(Dialogue_jpn[IDX].values[0]),
                           Place_jpn=Place_jpn[IDX].values[0],
                           Address_jpn=Address_jpn[IDX].values[0],
                           SubImage_jpn=SubImage_jpn[IDX])


@app.route("/map", methods=['GET', 'POST'])
def AllMap():
    return render_template('map.html')


app.run(host='0.0.0.0', port='80')
