import sys
import os
import pandas as pd
import webbrowser
from flask import Flask, request, render_template, jsonify

from src.exception import CustomException
from src.utils import load_object
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html', results=None)

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
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

        # Respond with JSON (for Fetch API)
        return jsonify({
            "predicted_score": round(results[0], 2),
            "inputs": request.form.to_dict()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    url = "http://127.0.0.1:5000/"
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        webbrowser.open_new_tab(url)

    app.run(host="0.0.0.0", debug=True)