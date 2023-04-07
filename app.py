from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.prdict_pipeline import CustomData,PredictPipeline
from src.logger import logging
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictions",methods=['GET','POST'])
def predictions():
    if(request.method =='GET'):
        return render_template("home.html")
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        dataframe_for_prediction = data.get_data_as_frame()
        logging.info(dataframe_for_prediction)
        predpipeline = PredictPipeline()
        result = predpipeline.predict(dataframe_for_prediction)
        return render_template('home.html',results = result[0])



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
