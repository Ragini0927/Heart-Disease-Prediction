import numpy as np
import pandas as pd
import pickle 
import streamlit as st
# loading the csv data to a Pandas DataFrame

# loading the saved model
loaded_model = pickle.load(open("C:/Users/HP/Desktop/Heart_Disease/Trained_model.pkl","rb"))

# creating a function for Prediction

def heart_Disease_prediction(input_data):

# change the input data to a numpy array
 input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
 input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

 prediction = loaded_model.predict(input_data_reshaped)
 print(prediction)

 if (prediction[0]== 0):
  return 'The Person does not have a Heart Disease'
 else:
  return 'The Person has Heart Disease'

def main():
    
    st.title('Heart Disease Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Age = st.text_input('Age of the Person')
    sex = st.text_input('Sex -0 for female and 1 for male')
    cp = st.text_input('cp')
    trestbps=st.text_input('trestbps')
    chol = st.text_input('chol')
    fbs = st.text_input('fbs')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')

    # code for Prediction
    diagnosis = ''    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_Disease_prediction([Age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang,oldpeak,slope,ca,thal])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
