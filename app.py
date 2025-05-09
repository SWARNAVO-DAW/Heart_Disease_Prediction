# import streamlit as st
# import pickle
# import numpy as np

# # Load the model
# model = pickle.load(open('Heart_Diesease.sav', 'rb'))

# # Title
# st.title('Heart Disease Prediction')

# # Input fields
# age = st.number_input('Age', (55))
# sex = st.selectbox('Sex', (1))  # 0: Female, 1: Male
# cp = st.selectbox('Chest Pain Type', (2))
# trestbps = st.number_input('Resting Blood Pressure', (140))
# chol = st.number_input('Serum Cholestoral (mg/dl)',(200))
# fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', (0))
# restecg = st.selectbox('Resting Electrocardiographic results', (1))
# thalach = st.number_input('Maximum Heart Rate Achieved', (170))
# exang = st.selectbox('Exercise Induced Angina', (0))
# oldpeak = st.number_input('ST depression induced by exercise' , (1.5))
# slope = st.selectbox('Slope of peak exercise ST segment', (2))
# ca = st.number_input('Number of major vessels (0-3)',3)
# thal = st.selectbox('Thalassemia', (3))

# # Prediction
# if st.button('Predict Heart Disease'):
#     input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak ,slope, ca, thal]]).reshape(1, -1)
#     prediction = model.predict(input_data)

#     if prediction[0] == 1:
#         st.success('The person has heart disease')
#     else:
#         st.success('The person does not have heart disease') 

import numpy as np
import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open('Heart_Diesease.sav', 'rb'))

# Title
st.title('Heart Disease Prediction Web App')

# Input fields
age = st.number_input('Age', min_value=1, max_value=100, step=1)
sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
cp = st.selectbox('Chest Pain Type (cp)', [1, 2, 3 , 4]) # 1: Typical Angina, 2: Atypical Angina, 3: Non-Anginal Pain, 4: Asymptomatic
trestbps = st.number_input('Resting Blood Pressure (trestbps)', min_value=50, max_value=250) # in mm Hg on admission to the hospital  
chol = st.number_input('Serum Cholesterol in mg/dl (chol)', min_value=100, max_value=600)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', [0, 1]) # 0: False, 1: True
restecg = st.selectbox('Resting Electrocardiographic Results (restecg)', [0, 1, 2]) # 0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy 
thalach = st.number_input('Maximum Heart Rate Achieved (thalach)', min_value=60, max_value=220)
exang = st.selectbox('Exercise Induced Angina (exang)', [0, 1]) # 0: No, 1: Yes
oldpeak = st.number_input('ST depression (oldpeak)', min_value=0.0, max_value=10.0, step=0.1) # ST depression induced by exercise relative to rest
slope = st.selectbox('Slope of Peak Exercise ST Segment (slope)', [1, 2, 3]) # 1: Upsloping, 2: Flat, 3: Downsloping
ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy (ca)', [0, 1, 2, 3, 4])
thal = st.selectbox('Thalassemia (thal)', [0, 1, 2, 3]) # 0: Normal, 1: Fixed Defect, 2: Reversible Defect, 3: No Defect or 3 = normal; 6 = fixed defect; 7 = Reversible defect 

# Prediction
if st.button('Predict Heart Disease'):
    input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                           thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('The person is likely to have heart disease.')
    else:
        st.success('The person is not likely to have heart disease.')
