import pandas as pd
import numpy as np
import streamlit as st
import pickle 
import json

with open('HousePricePrediction.pkl','rb') as f:
    classifier = pickle.load(f)

with open('columns_info.json','r') as  f:
    data_col = json.load(f)['data_col']

def price_prediction(location,sqft,bath,bhk):
    col = data_col
    x = np.zeros(len(col))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location in col:
        loc_index = col.get_loc(location)
        x[loc_index] = 1
    return classifier.predict([x])[0]

def main():
    st.title('House Price Prediction in Bangalore')
    html_temp = """
     <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit House Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html = True)
    location = st.text_input('Location')
    sqft = st.text_input('Square Feet')
    bath = st.text_input('Bathrooms')
    bhk = st.text_input('BHK')

    result = ''
    if st.button('Show Amount'):
        result = (price_prediction(location,sqft,bath,bhk))*100000
    st.success('The price is {}'.format(result))


if __name__ == '__main__':
    main()