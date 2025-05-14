from flask import Flask, render_template, request, jsonify
from connect import Prediction
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    prediction_obj = Prediction()
    
    # Get the text input from the form
    text_input = request.form['text_input']
    
    # Translate the text to English
    translated_text = translator.translate(text_input, dest='en').text
    
    # Get the prediction for the translated text
    result = prediction_obj.get_prediction(translated_text)
    
    # Pass the translated text and prediction result to the template
    return render_template('index.html', text_input=text_input, translated_text=translated_text, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
