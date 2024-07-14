import pickle
from flask import Flask, render_template, request
import pandas as pd

import numpy as np
model1 = pickle.load(open('model.pkl','rb'))

Battery_life_le = pickle.load(open('Battery_life_le.pkl','rb'))
Brand_le = pickle.load(open('Brand_le.pkl','rb'))
Connectivity_le = pickle.load(open('Connectivity_le.pkl','rb'))
Display_Type_le = pickle.load(open('Display_Type_le.pkl','rb'))
GPS_le = pickle.load(open('GPS_le.pkl','rb'))
Model_le = pickle.load(open('Model_le.pkl','rb'))
NFC_le = pickle.load(open('NFC_le.pkl','rb'))
Operating_System_le = pickle.load(open('Operating_System_le.pkl','rb'))
Resolution_le = pickle.load(open('Resolution_le.pkl','rb'))
Water_Resistance_le = pickle.load(open('Water_Resistance_le.pkl','rb'))

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/brands')
def brands():
    return render_template('brands.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    print("hi")
    if request.method == 'POST' :
        brand = request.form['brand']
        model = request.form['model']
        os = request.form['os']
        connectivity = request.form['connectivity']
        display_type = request.form['display-type']
        display_size = request.form['display-size']
        resolution = request.form['resolution']
        water_resistance = request.form['water-resistance']
        battery_life = request.form['battery-life']
        heart_rate_monitor = request.form['heart-rate-monitor']
        gps = request.form['gps']
        nfc = request.form['nfc']
        
        brand = Brand_le.transform([brand])
        model = Model_le.transform([model])
        os = Operating_System_le.transform([os])
        connectivity = Connectivity_le.transform([connectivity])
        display_type = Display_Type_le.transform([display_type])
        display_size = float(display_size)
        print(resolution)
        resolution = Resolution_le.transform([resolution])
        water_resistance = float(water_resistance)
        battery_life = float(battery_life)
        heart_rate_monitor = float(heart_rate_monitor)
        gps = GPS_le.transform([gps])
        nfc = NFC_le.transform([nfc])

        column_names = ['Brand','Model','Operating System','Connectivity','Display Type','Display Size','Resolution','Water Resistance','Battery Life','Heart Rate Monitor','GPS','NFC']
        x=[brand,model,os,connectivity,display_size,display_type,resolution,water_resistance,battery_life,heart_rate_monitor,gps,nfc]
        df = pd.DataFrame([x])
        print('working')
        df.columns = column_names
        print(df)
        pred=model1.predict(df)
        print(pred)
        return render_template('watch_prediction.html',pred = pred)
    return render_template('predict.html')



if __name__ == '__main__':
    app.run(debug=True)
     