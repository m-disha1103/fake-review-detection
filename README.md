# 🧠 Fake Review Detection System

An AI-powered web application that detects whether an online review is **Fake ❌** or **Genuine ✅** using Natural Language Processing (NLP) and Machine Learning.

---

## 🚀 Live Demo

🌐 https://fake-review-detection-8en8.onrender.com

---

## 📌 Features

* 🔍 Detects fake vs genuine reviews
* 🧠 Uses NLP (Text Cleaning + TF-IDF)
* 🤖 Machine Learning model (Logistic Regression)
* 🌙 Dark mode support
* ⏳ Loading animation
* 📊 Confidence score & probability display
* ⚠️ Input validation
* 🌐 Fully deployed web application

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Machine Learning:** Scikit-learn
* **NLP:** NLTK, TextBlob
* **Deployment:** Render
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
fake-review-detector/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── data/
│   └── raw/
│       └── reviews.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ How It Works

1. User enters a review
2. Text is cleaned and preprocessed
3. TF-IDF converts text → numerical features
4. ML model predicts:

   * Fake ❌
   * Genuine ✅
5. Displays result with confidence score

---

## ▶️ Run Locally

```bash
# Clone repository
git clone https://github.com/your-username/fake-review-detector.git

# Go to project folder
cd fake-review-detector

# Install dependencies
pip install -r requirements.txt

# Run app
python app/app.py
```

---

## 📸 Screenshot

(Add your app screenshot here)

```
Example:
![App Screenshot](screenshot.png)
```

---

## 📊 Model Details

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF
* Dataset: Amazon Reviews Dataset
* Accuracy: ~80–90%

---

## 🚧 Future Improvements

* 🔥 Use advanced models (BERT, Transformers)
* 📱 Make UI fully responsive
* 📊 Add analytics dashboard
* 🧠 Improve dataset quality
* 🔐 Add security & API layer

---

## 👩‍💻 Author

**Disha Malviya**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
