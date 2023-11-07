# Import libraries
import pandas as pd             # Pandas
import streamlit as st          # Streamlit
import matplotlib.pyplot as plt # Matplotlib
import seaborn as sns           # Seaborn

# Module to save and load Python objects to and from files
import pickle 

import warnings
warnings.filterwarnings('ignore')

st.title('Bike Usage Regression')

bike_file = st.file_uploader('Please provide a dataset to use with the ML model')

# USER MANUAL INPUT
with st.form('user_inputs'):
    season = st.selectbox('Season?', options=['Winter','Spring','Summer','Fall'])
    mnth = st.selectbox('Month?', options= ['January','February','March','April','May','June','July','August','September','October','November','December'])
    holiday = st.selectbox('Holiday?', options=['No','Yes'])
    weekday = st.selectbox('Day of the Week?', options=['Monday','Tuesday','Wednesday','Thrusday','Friday'])
    workingday = st.selectbox('Weekday?', options=['No','Yes'])
    weathersit = st.selectbox('Weather Situation', options=['Clear','Misty','Light Snow/Rain','Heavy Snow/Rain'])
    temp = st.number_input('Normalized Temperature: please provide a value between 0 and 1', min_value=0, max_value=1)
    atemp = st.number_input('Felt Temperature: please provide a value between 0 and 1', min_value=0, max_value=1)
    hum = st.number_input('Humidity: please provide a value between 0 and 1', min_value=0, max_value=1)
    windspeed = st.number_input('Windspeec: please provide a value between 0 and 1', min_value=0, max_value=1)
    st.form_submit_button()
# USE PICKLE FILE!!
if bike_file is None:
    newprediction = bk_r.predict([[season,mnth,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed]])
    st.subheader('The predicted amount of bikes is {}'.format())
else:
    user_df = pd.read_csv(bike_file)
    original_df = pd.read_csv('bike.csv')

    #drop nulls
    user_df = user_df.dropna() 
    original_df = original_df.dropna()

    original_df = original_df.drop(columns = ['cnt', 'yr'])

    user_df = user_df[original_df.columns]

    combined_df = pd.concat([original_df, user_df], axis = 0)

    original_rows = original_df.shape[0]

    combined_df_encoded = pd.get_dummies(combined_df)
    original_df_encoded = combined_df_encoded[:original_rows]
    user_df_encoded = combined_df_encoded[original_rows:]
    user_pred_cnt = bk_r.predict(user_df_encoded)
    user_df['Predicted Count'] = user_pred_cnt
    st.subheader('Predicting your Bike Rental Count')
    st.write(user_df)

st.subheader('Prediction Performance')
tab1, tab2 = st.tabs(['Decision Tree','Feature Importance'])

with tab1:

with tab2:



# when using form values, concat will not work, must learn how to append row to original data frame and then get dummies, 