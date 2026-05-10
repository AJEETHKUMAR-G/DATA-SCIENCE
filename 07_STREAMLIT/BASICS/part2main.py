import streamlit as st
import time as ts
img = st.file_uploader("Upload your file: ",type = ["png","jpg","jpeg"],accept_multiple_files=True)
#accept_multiple_files=True this parameter gives access to upload multiple files
#type = ["png","jpg","jpeg"]
if img is not None:
    #st.video(img)
    for i in img:
        st.image(i,width=250)
st.markdown("---")

#st.slider("Rate the work")
st.slider("Rate the work",min_value = 50,max_value = 200,value = 89)

st.text_input("Enter your course title:",max_chars=15)

st.text_area("Feedback:",max_chars=100)

st.date_input("Enter the DOB:")
st.time_input("Enter the time:")

bar = st.progress(0)
for i in range(10):
        bar.progress((i+1)*10)
        ts.sleep(2)
        
