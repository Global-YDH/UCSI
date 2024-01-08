#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pickle
import pandas as pd
import streamlit as st 

pickle_in = open("RF.pkl","rb")
rf=pickle.load(pickle_in)


def predict_std_perf(hour_s, pre_score):
    prediction=rf.predict([[hour_s, pre_score]])
    print(prediction)
    return prediction

def main():
    st.title("Student Performance Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    hour_s = st.text_input("hour of study","Type Here")
    pre_score = st.text_input("previous score", "Type Here")
    result=""
    if st.button("Predict"):
        result=predict_std_perf(hour_s, pre_score)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn Python")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()

