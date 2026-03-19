# 💳 Credit Card Fraud Detection System

An end-to-end **Machine Learning project** that detects fraudulent credit card transactions using advanced data analysis, model building, and deployment techniques.

---

## 🚀 Project Overview

This project aims to identify fraudulent transactions from a highly imbalanced dataset using machine learning models. It includes:

* Data preprocessing & feature engineering
* Model training using Random Forest
* REST API using Flask
* Interactive dashboard using Streamlit
* Explainable AI using SHAP

---

## 📊 Dataset

* Source: Kaggle Credit Card Fraud Detection Dataset
* Transactions: 284,807
* Fraud cases: 492 (~0.17%)
* Highly imbalanced dataset

👉 Download dataset:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## 🧠 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Flask (API)
* Streamlit (UI)
* SHAP (Explainable AI)
* Matplotlib, Seaborn

---

## ⚙️ Project Structure

```
credit-card-fraud-detection
│
├── app/                # Flask API
├── src/                # ML pipeline & training
├── notebooks/          # EDA notebook
├── models/             # Saved model (ignored in Git)
├── data/               # Dataset (ignored in Git)
├── streamlit_app.py    # Dashboard UI
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Add Dataset

Download dataset and place it inside:

```
data/creditcard.csv
```

---

### 4️⃣ Train Model

```
python src/train_model.py
```

---

### 5️⃣ Run Flask API

```
python app/app.py
```

API runs on:

```
http://127.0.0.1:5000
```

---

### 6️⃣ Run Streamlit Dashboard

```
streamlit run streamlit_app.py
```

Dashboard runs on:

```
http://localhost:8501
```

---

## 🔍 Features

* Fraud detection using ML
* Handles imbalanced dataset
* Real-time prediction API
* Interactive UI dashboard
* Model explainability using SHAP

---

## 📈 Future Improvements

* Use XGBoost / LightGBM for better performance
* Apply SMOTE for imbalance handling
* Deploy on cloud (AWS / Render / HuggingFace)
* Add user authentication
* Improve UI design

---

## 📸 Demo 

<img width="1648" height="841" alt="image" src="https://github.com/user-attachments/assets/a13fa44b-2fd4-4dcf-b1a4-957fb6d61beb" />
<img width="1289" height="257" alt="image" src="https://github.com/user-attachments/assets/63a7e296-d0e2-4aa3-a669-5b932234d6b8" />

<img width="968" height="796" alt="image" src="https://github.com/user-attachments/assets/e53acb75-6bb2-4bb0-b920-09f50109822d" />


---

## 👨‍💻 Author

**Ankit Katre**
Aspiring Data Scientist

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---

