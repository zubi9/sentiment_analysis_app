from flask import Flask, jsonify, render_template, request
from utilities import predict_pipeline

app = Flask(__name__)

# Function to predict sentiment (a placeholder for your actual model)
def predict_sentiment(text):
    if len(text) > 0 and text not in [chr(i) for i in range(256)]:
        result = predict_pipeline([text])[0]
        return result
    else:
        raise ValueError("Please enter text for prediction,\
                          It is hard to make inference with single charactor, Thanks")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_result = None
    if request.method == 'POST':
        try:
            text = request.form['text']
            prediction_result = predict_sentiment(text)
        except ValueError as e:
            prediction_result = {'error': str(e)}
    return render_template('index.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
