# 🧠 Emotion Classification from Text (Classical ML + Streamlit)

## 📌 Overview
This project builds an **emotion classification system** that predicts emotions from text using **classical machine learning (no deep learning)**.

It combines:
- **TF-IDF features**
- **Lexicon-based features**
- **Naive Bayes & Logistic Regression**

The model is deployed as a **live web application** using Streamlit.

---

## 🌐 Live Demo

👉 **Try the app here:**  
[Emotion Classification from Text](https://emotion-classification-from-text-using-classical-machine-learn.streamlit.app/)

---

## 🎯 Objectives
- Classify text into:
  - 😊 Happy
  - 😢 Sad
  - 😡 Angry
  - 😨 Fear
- Use interpretable machine learning techniques
- Compare multiple ML models
- Improve accuracy using larger datasets
- Build a real-time prediction system

---

## 📊 Dataset Improvement

| Stage        | Dataset Size |
|-------------|-------------|
| Initial     | ~2,000 rows |
| Updated     | ~16,000 rows |

👉 Increasing dataset size improved:
- Model generalization  
- Prediction reliability  
- Overall accuracy  

---

## 📈 Model Performance Comparison

### 🔹 Before Dataset Expansion

| Model                | Accuracy |
|---------------------|----------|
| Naive Bayes         | 0.6084   |
| Logistic Regression | 0.7042   |

---

### 🔹 After Dataset Expansion

| Model                | Accuracy |
|---------------------|----------|
| Naive Bayes         | 0.7833   |
| Logistic Regression | 0.9154   |

---
## 📊 Accuracy Improvement Visualization

![Accuracy Comparison](accuracy_comparison.png)

This graph shows the improvement in model performance after increasing the dataset size from 2,000 to 16,000 samples.

## 📊 Confusion Matrix

![Confusion Matrix](confusion_matrix.png)

The confusion matrix shows how well the model classifies each emotion.  
Diagonal values represent correct predictions, while off-diagonal values indicate misclassifications.

---

## 🧠 Model Explanation

### 🔹 Why Logistic Regression performed better?

- It handles high-dimensional data efficiently  
- Works well with TF-IDF features  
- Captures relationships between features better than Naive Bayes  
- Provides better separation between emotion classes  

### 🔹 Why Naive Bayes performed lower?

- Assumes feature independence (which is not always true in text data)  
- Less effective when features are correlated  

### 🔹 Key Insight

Increasing dataset size significantly improved performance because:
- More data → better generalization  
- Reduced overfitting  
- Improved pattern recognition  

👉 Final model: **Logistic Regression**

---

## 🚀 Improvement Analysis

- Accuracy improved significantly after increasing dataset size  
- Naive Bayes improved by **~17%**  
- Logistic Regression improved by **~21%**  
- Logistic Regression clearly performs better for this task  

---

## ⚙️ Methodology

### 🔹 Data Preprocessing
- Convert text to lowercase  
- Remove special characters  
- Clean text  

### 🔹 Feature Engineering

#### 📊 TF-IDF
- Converts text into numerical form  
- Captures word importance  
- Limited to 3000 features  

#### 📘 Lexicon Features
- Counts emotion-related words  
- Adds human knowledge  
- Improves interpretability  

---

## 🤖 Models Used

### 1️⃣ Naive Bayes
- Simple and fast  
- Suitable for text classification  

### 2️⃣ Logistic Regression (Final Model ✅)
- Better performance  
- Handles complex patterns  
- Higher accuracy  

---

## 🔄 Pipeline
1. Text Cleaning  
2. TF-IDF Extraction  
3. Lexicon Feature Extraction  
4. Feature Combination  
5. Model Training  
6. Prediction  

---

## 🌐 Deployment
The model is deployed using **Streamlit**, enabling:
- Real-time text input  
- Instant emotion prediction  
- Interactive UI  

---

## 💡 Key Features
- Classical ML (No Deep Learning)  
- Model Comparison (NB vs LR)  
- Improved Accuracy with Larger Dataset  
- Real-time Predictions  
- Live Web Application 🌐  

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

---

## 📸 Example
**Input:**

I am feeling very happy today


**Output:**

😊 Happy

---

## 🔮 Future Improvements
- Add more emotion categories  
- Try advanced ML/DL models  
- Improve feature engineering  
- Enhance UI/UX  

---

## 🎓 Conclusion
Increasing the dataset size from **2,000 to 16,000 samples** significantly improved model performance.

- Logistic Regression achieved the best accuracy (**91.54%**)  
- Dataset scaling played a crucial role in improving results  
- The project demonstrates the importance of data quality in machine learning  

---

## 👩‍💻 Author
**Akanksha Naidu**  
MSc Big Data Analytics  

---

## 📌 License
This project is for academic and learning purposes.
