# 🧠 Emotion Classification from Text (Classical ML + Streamlit)

## 📌 Overview
This project builds an **emotion classification system** that predicts emotions from text using **classical machine learning (no deep learning)**.

It combines:
- **TF-IDF features**
- **Lexicon-based features**
- **Logistic Regression**

The model is deployed as a **Streamlit web application** for real-time predictions.

---

## 🎯 Objectives
- Classify text into:
  - 😊 Happy
  - 😢 Sad
  - 😡 Angry
  - 😨 Fear
- Use interpretable machine learning techniques
- Combine statistical and rule-based features
- Build a real-time prediction system

---

## ⚙️ Methodology

### 🔹 Data Preprocessing
- Convert text to lowercase
- Remove special characters
- Clean text for consistency

### 🔹 Feature Engineering

#### 📊 TF-IDF
- Converts text into numerical form
- Captures importance of words
- Limited to 3000 features

#### 📘 Lexicon Features
- Counts emotion-related words
- Adds human knowledge to the model
- Improves interpretability

---

## 🤖 Model
- Logistic Regression (Multi-class classification)
- Chosen for:
  - Simplicity
  - Interpretability
  - Efficiency

---

## 🔄 Pipeline
1. Text Cleaning  
2. TF-IDF Extraction  
3. Lexicon Feature Extraction  
4. Feature Combination  
5. Model Training  
6. Prediction  

---

## 📈 Evaluation
- Accuracy Score  
- Confusion Matrix  
- Classification Report  

---

## 🌐 Deployment
The model is deployed using **Streamlit**, enabling:
- Real-time text input
- Instant emotion prediction
- Interactive UI

---

## 💡 Key Features
- Classical ML (No Deep Learning)
- Interpretable Model
- Fast and Lightweight
- Real-time Predictions
- Simple UI

---

## 🗂️ Project Structure
ML Project/

│

├── train_model.ipynb

├── app.py

├── model.pkl

├── tfidf.pkl

├── test.csv

└── README.md


---

## 🛠️ Technologies Used
- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Streamlit  
- Matplotlib  
- Seaborn  

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
pip install scikit-learn pandas numpy scipy matplotlib seaborn streamlit

### 2️⃣ Train the Model
Run:
train_model.ipynb

This generates:
- model.pkl  
- tfidf.pkl  

### 3️⃣ Run the App
streamlit run app.py


### 4️⃣ Open in Browser

[Emotion-Classification](https://emotion-classification-from-text-using-classical-machine-learn.streamlit.app/)


---

## 📸 Example
**Input:**

I am feeling very happy today


**Output:**

😊 Happy


---

## 🔮 Future Improvements
- Add more emotion classes  
- Improve dataset  
- Try advanced models  
- Deploy online  

---

## 🎓 Conclusion
This project demonstrates that **classical machine learning combined with feature engineering** can effectively perform emotion classification while remaining interpretable and efficient.

---

## 👩‍💻 Author
Akanksha Naidu  
MSc Big Data Analytics  

---

## 📌 License
This project is for academic and learning purposes.
