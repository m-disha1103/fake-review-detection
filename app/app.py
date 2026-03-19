from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model safely
try:
    model = pickle.load(open('../model/model.pkl', 'rb'))
    vectorizer = pickle.load(open('../model/vectorizer.pkl', 'rb'))
    print("Model loaded successfully ✅")
except Exception as e:
    print("Error loading model:", e)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    
    if request.method == 'POST':
        review = request.form['review']
        
        try:
            vec = vectorizer.transform([review])
            prediction = model.predict(vec)[0]
            prob = model.predict_proba(vec)[0]

            confidence = max(prob) * 100

            if prediction == 1:
                result = "❌ Fake Review"
            else:
                result = "✅ Genuine Review"

        except Exception as e:
            result = "Error: " + str(e)
            confidence = 0

    return render_template('index.html', result=result, confidence=round(confidence, 2))

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))