import sys
import os
import pandas as pd
import webbrowser
from flask import Flask, request, render_template

from src.exception import CustomException
from src.utils import load_object
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Tell Flask where to find the templates
app = Flask(__name__, template_folder='templates')

# --- Routes ---
@app.route('/')
def home():
    # This route will render your home.html file
    return render_template('home.html', results=None)

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            pred_df = data.get_data_as_data_frame()
            print("Input DataFrame:\n", pred_df)

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            return render_template('home.html', results=round(results[0], 2))

        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == '__main__':
    # The URL for your Flask app
    url = "http://127.0.0.1:5000/"

    # Open the URL in a new browser tab
    webbrowser.open_new_tab(url)

    # Run the Flask app
    app.run(host="0.0.0.0", debug=True)