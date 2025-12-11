import pandas as aju
import pickle
import streamlit as st
import numpy as np

pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

def prediction_auth(variance,skewness,curtosis,entropy):
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return prediction


def main():
    st.title("Bank Authenticator")
    html_temp = """
     <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html = True)
    variance = st.text_input("Variance","Type here")
    skewness = st.text_input("skewness","Type here")
    curtosis = st.text_input("Curtosis","Type here")
    entropy = st.text_input("Entropy","Type here")

    result = ""
    if st.button("predict"):
        result = prediction_auth(variance,skewness,curtosis,entropy)
    st.success('The Output is {}'.format(result))
    if st.button('About'):
        st.text('Built by Ajeeth')
        st.text('Jr. Data Scientist')
    
if __name__ =='__main__':
    main()
