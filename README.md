# Heart_Disease_Prediction 
This project is a complete machine learning workflow that predicts whether a person is likely to have heart disease based on key clinical features. The solution includes a Jupyter Notebook for model development, a Streamlit web app for user interaction, and deployment-ready files.

📊 Dataset
Source: UCI / Kaggale

Rows: 303

Columns: 14 (13 features + 1 target)

Target Variable: target

1 = presence of heart disease

0 = absence of heart disease 

🔍 Features Used
age, sex, cp, trestbps, chol, fbs, restecg,
thalach, exang, oldpeak, slope, ca, thal

Each represents clinical attributes such as blood pressure, cholesterol, ECG results, chest pain type, etc. 

🧠 Model Building
Models used:

Logistic Regression

Decision Tree

Evaluation Metrics:

Accuracy: ~91%

F1-Score: ~0.92

ROC AUC Score: High

Final model saved as: Heart_Diesease.sav 

🖥️ Web App (Streamlit)
A lightweight web application (app.py) was developed using Streamlit where users can input values for 13 features and receive an instant prediction.

✅ Real-time results
✅ User-friendly interface
✅ Fast and portable 

🧪 How to Run
Clone this repo

Install dependencies:

pip install streamlit pandas numpy scikit-learn
Run the app:

streamlit run app.py or python -m streamlit run app.py 
Enter clinical data in the form and get prediction 

⚙️ Requirements
Python 3.8+

Streamlit

scikit-learn

pandas, numpy, matplotlib, seaborn (for notebook) 

🚀 Future Enhancements
Host the app on Streamlit Cloud

Add more Predictions Systems

Add deep learning models

Integrate real-time wearable data (API)

Mobile UI improvements
