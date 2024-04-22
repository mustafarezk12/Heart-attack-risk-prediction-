import pickle
import streamlit as st
import pandas as pd
import numpy as np

import time

model = pickle.load(open('model.pkl','rb'))

def heart_attack_prediction(input_data):
     #changing the input data to numpy array 
     input_data_as_numpy_array=np.asanyarray(input_data)

     #reshape the array as we are predictiog
     input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
     prediction=model.predict(input_data_reshape)

     if (prediction[0]== 0):
      return "you don't have propability to have heart attack"
     else:
         return "you have heart attack chec kthe doctor "




def main():
    st.title('heart ayttack prediction')
    age = st.number_input('Enter your age:  Between 29 to 90 ')
    sex  = st.selectbox('Sex 0-Female 1-Male',(0,1))
    cholesterol = st.number_input('Serum cholestoral in mg/dl: Between 126 to 564 ')
    heartrate	 = st.number_input('Maximum heart rate achieved: Between 71 to 202 ')
    diabetes  = st.selectbox('Whether the patient has diabetes (1:Yes/0:No)',(0,1))
    familyhistory= st.selectbox('Family history of heart-related problems (1: Yes, 0: No)',(0,1))
    smoking  = st.selectbox('Smoking status of the patient (1: Smoker, 0: Non-smoker',(0,1))
    obesity  = st.selectbox('Obesity 0-Female 1-Male',(0,1))
    exercisehoursperweek = st.number_input('Exercise Hours Per Week	 Between 29 to 90 ')
    diet  = st.selectbox('Diet 0-no diet 1-diet ',(0,1,2))
    previousheartproblems = st.selectbox('previous problem 0 no 1 yes',(0,1))
    medicationuse = st.selectbox('medication use 0 no use 1 use',(0,1))
    sedentaryhoursperday = st.number_input('sedentary hours per day ')
    bmi = st.number_input('Your Body Mass Index')
    triglycerides = st.number_input('Triglycerides are a type of fat, called lipids , that circulate in your blood. They are the most common type of fat in your body. Triglycerides come from foods, especially butter, oils, and other fats you eat. ')
    physicalactivitydaysperWeek	= st.number_input(' physical activity days per Week')
    sleephoursperday = st.number_input('sleephoursperday ')
    BP_Systolic = st.number_input('The first number, called systolic blood pressure, is the pressure caused by your heart contracting and pushing out blood.   ')
    BP_Diastolic = st.number_input(' The second number, called diastolic blood pressure, is the pressure when your heart relaxes and fills with blood. ')
    makeprediction= ''
 #prediction code
    if st.button('predict'):
         data=np.array([[age,sex,cholesterol,heartrate,diabetes,familyhistory,smoking,obesity,exercisehoursperweek,diet,previousheartproblems,medicationuse,sedentaryhoursperday,bmi,triglycerides,physicalactivitydaysperWeek,sleephoursperday,BP_Systolic,BP_Diastolic]])
         makeprediction = heart_attack_prediction(data)
         st.success(makeprediction)



if __name__=='__main__':
     main()


