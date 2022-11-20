from flask import Flask,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)

#load model
model=pickle.load(open('savedmodel1 (1).sav','rb'))

@app.route('/')
def home():
    result=''
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    SL=float(request.form['SL'])
    SW=float(request.form['SW'])
    PL=float(request.form['PL'])
    PW=float(request.form['PW'])
    result=model.predict([[SL,SW,PL,PW]])[0]
    return render_template('index.html',**locals())


if __name__ == '__main__':
    app.run(debug=True)



