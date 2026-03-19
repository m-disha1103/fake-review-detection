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
    confidence = 0
    fake_prob = 0
    real_prob = 0

    if request.method == 'POST':
        review = request.form['review']

        try:
            vec = vectorizer.transform([review])
            prediction = model.predict(vec)[0]

            if hasattr(model, "predict_proba"):
                prob = model.predict_proba(vec)[0]
                confidence = max(prob) * 100
                fake_prob = prob[1] * 100
                real_prob = prob[0] * 100

            result = "❌ Fake Review" if prediction == 1 else "✅ Genuine Review"

        except Exception as e:
            result = "Error: " + str(e)

    return render_template(
        'index.html',
        result=result,
        confidence=round(confidence, 2),
        fake_prob=round(fake_prob, 2),
        real_prob=round(real_prob, 2)
    )

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))