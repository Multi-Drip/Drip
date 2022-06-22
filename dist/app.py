from flask import Flask, request, render_template, redirect
from flask_cors import CORS
import re
import random
import pandas as pd
import numpy as np
import os
from flask import Markup

app = Flask(__name__, static_url_path="/static")
Data = pd.read_csv("Data.csv")
Data = Data.drop(['roadmap_ox','modified_La','modified_Lo'], axis=1)
Data = Data.dropna()
#cwd = os.getcwd()
#files = os.listdir(cwd)

CORS(app)

MainImage = Data['MainImage']
Title = Data['Title']
Title_eng = Data['EngTitle']
Title_jpn = Data['JpnTitle']
DataFilter = Data['DataFilter']
PlaceFilter = Data['PlaceFilter']
Subtitle = Data['Subtitle']
Subtitle_eng=Data['EngSubtitle']
Subtitle_jpn=Data['JpnSubtitle']
DramaPlace = Data['DramaPlace']
DramaPlace_eng = Data['EngDramaPlace']
DramaPlace_jpn = Data['JpnDramaPlace']
Dialogue = Data['Dialogue']
Dialogue_eng = Data['EngDialogue']
Dialogue_jpn = Data['JpnDialogue']
Place = Data['Place']
Place_eng = Data['EngPlace']
Place_jpn = Data['JpnPlace']
Address = Data['Address']
Address_EJ = Data['EJAddress']
LatitudeValue = Data['LatitudeValue']
LongitudeValue = Data['LongitudeValue']
SubImage = Data['SubImage']

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
                            len = len(DramaPlace_eng),
                            DataFilter_eng=DataFilter,
                            Place_eng=Place_eng,
                            MainImage_eng=MainImage,
                            Title_eng=Title_eng,
                            Subtitle_eng=Subtitle_eng)
@app.route("/jpnmain", methods=['GET', 'POST'])
def JpnMain():
    return render_template('jpnmain.html',
                            len = len(DramaPlace_jpn),
                            DataFilter_jpn=DataFilter,
                            Place_jpn=Place_jpn,
                            MainImage_jpn=MainImage,
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

# 1. 전주
@app.route("/coursejj", methods=['GET', 'POST'])
def coursejj():
    return render_template('course01jj.html')
@app.route("/coursejj_jpn", methods=['GET', 'POST'])
def coursejj_jpn():
    return render_template('course01jj_jpn.html')
@app.route("/coursejj_eng", methods=['GET', 'POST'])
def coursejj_eng():
    return render_template('course01jj_eng.html')

# 2. 경주
@app.route("/coursegj", methods=['GET', 'POST'])
def Coursegj():
    return render_template('course02gj.html')
@app.route("/coursegj_jpn", methods=['GET', 'POST'])
def Coursegj_jpn():
    return render_template('course02gj_jpn.html')
@app.route("/coursegj_eng", methods=['GET', 'POST'])
def Coursegj_eng():
    return render_template('course02gj_eng.html')

# 3. 강원
Gw = pd.read_csv("gangwon_place.csv")
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
EngGwName = Gw['engname']
EngGwDistance = Gw['engdistance']
EngGwDetail = Gw['engdetail']
@app.route("/coursegw_eng", methods=['GET','POST'])
def Coursegw_eng():
    return render_template('course03gw_eng.html',
                            lengw = len(EngGwName),
                            GwFilter = GwFilter,
                            EngGwName = EngGwName,
                            EngGwDistance = EngGwDistance,
                            GwImg = GwImg,
                            GwLink = GwLink,
                            EngGwDetail = EngGwDetail)
JpnGwName = Gw['jpnname']
JpnGwDistance = Gw['jpndistance']
JpnGwDetail = Gw['jpndetail']
@app.route("/coursegw_jpn", methods=['GET','POST'])
def Coursegw_jpn():
    return render_template('course03gw_jpn.html',
                            lengw = len(JpnGwName),
                            GwFilter = GwFilter,
                            JpnGwName = JpnGwName,
                            JpnGwDistance = JpnGwDistance,
                            GwImg = GwImg,
                            GwLink = GwLink,
                            JpnGwDetail = JpnGwDetail)

# 4. 서울
@app.route("/coursesu", methods=['GET', 'POST'])
def Coursesu():
    return render_template('course04su.html')
@app.route("/coursesu_jpn", methods=['GET', 'POST'])
def Coursesu_jpn():
    return render_template('course04su_jpn.html')
@app.route("/coursesu_eng", methods=['GET', 'POST'])
def Coursesu_eng():
    return render_template('course04su_eng.html')


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
                            DataFilter_eng=DataFilter[IDX],
                            LatitudeValue_eng=LatitudeValue[IDX].values[0],
                            LongitudeValue_eng=LongitudeValue[IDX].values[0],
                            Dialogue_eng=Markup(Dialogue_eng[IDX].values[0]),
                            Place_eng=Place_eng[IDX].values[0],
                            Address_eng=Address_EJ[IDX].values[0],
                            SubImage_eng=SubImage[IDX])

@app.route("/jpnsub", methods=['GET', 'POST'])
def JpnSub():
    InputPlace_jpn = request.args.get('Place')
    IDX = np.where(Place_jpn == InputPlace_jpn)[0]
    return render_template('jpnsub.html',
                            DramaPlace_jpn=DramaPlace_jpn[IDX].values[0],
                            DataFilter_jpn=DataFilter[IDX],
                            LatitudeValue_jpn=LatitudeValue[IDX].values[0],
                            LongitudeValue_jpn=LongitudeValue[IDX].values[0],
                            Dialogue_jpn=Markup(Dialogue_jpn[IDX].values[0]),
                            Place_jpn=Place_jpn[IDX].values[0],
                            Address_jpn=Address_EJ[IDX].values[0],
                            SubImage_jpn=SubImage[IDX])


@app.route("/map", methods=['GET', 'POST'])
def AllMap():
    return render_template('map.html')


app.run(host='0.0.0.0', port='80')
