import streamlit as st
import time as ts
st.markdown("<h1 style='text-align:center'>Registeration <i>Form</i></h1>",unsafe_allow_html=True)
st.sidebar.write("## **Choose the category** ")
st.sidebar.write("*You need to apply:*")
st.sidebar.caption("(Choose only one)")

opt = st.sidebar.radio("Click the Domain:",options=("Data science","Data Analytics","Full stack-java","Full stack-python","Machine Learning"))

if opt == "Data science":
    with st.form("DS",clear_on_submit = True,border = True):
        st.subheader("Data science registration form")
        f_n,l_n = st.columns(2)
        f_n.text_input("First Name")
        l_n.text_input("Last Name")
        st.text_input("Email address")
        age,course = st.columns(2)
        age.text_input("Age")
        course.text_input("Current Studies")
        st.slider("Rate Your Coding knowledge",min_value = 15)
        
        img = st.file_uploader("Upload your ID proof",type = ["png","jpg","jpeg"],accept_multiple_files= False)
        if img is not None:
            for i in img:
                st.image(i,width=500)
        st.checkbox("Not a robot",value = False)
        status = st.form_submit_button("Finished")
        if status:
            bar = st.progress(0)
            progress_stat = st.empty()
            for i in range(10):
                bar.progress((i+1)*10)
                check = progress_stat.write(str((i+1)*10)+"%")
                ts.sleep(1)
elif opt == "Data Analytics":
    with st.form("DA",clear_on_submit = True,border = True):
        st.subheader("Data Analytics registration form")
        f_n,l_n = st.columns(2)
        f_n.text_input("First Name")
        l_n.text_input("Last Name")
        st.text_input("Email address")
        age,course = st.columns(2)
        age.text_input("Age")
        course.text_input("Current Studies")
        st.slider("Rate Your Coding knowledge",min_value = 15)
        
        img = st.file_uploader("Upload your ID proof",type = ["png","jpg","jpeg"],accept_multiple_files= False)
        if img is not None:
            for i in img:
                st.image(i,width=500)
        st.checkbox("Not a robot",value = False)
        status = st.form_submit_button("Finished")
        if status:
            bar = st.progress(0)
            progress_stat = st.empty()
            for i in range(10):
                bar.progress((i+1)*10)
                check = progress_stat.write(str((i+1)*10)+"%")
                ts.sleep(1)
elif opt == "Full stack-java":
    with st.form("FSJ",clear_on_submit = True,border = True):
        st.subheader("Full stack-java registration form")
        f_n,l_n = st.columns(2)
        f_n.text_input("First Name")
        l_n.text_input("Last Name")
        st.text_input("Email address")
        age,course = st.columns(2)
        age.text_input("Age")
        course.text_input("Current Studies")
        st.slider("Rate Your Coding knowledge",min_value = 15)
        
        img = st.file_uploader("Upload your ID proof",type = ["png","jpg","jpeg"],accept_multiple_files= False)
        if img is not None:
            for i in img:
                st.image(i,width=500)
        st.checkbox("Not a robot",value = False)
        status = st.form_submit_button("Finished")
        if status:
            bar = st.progress(0)
            progress_stat = st.empty()
            for i in range(10):
                bar.progress((i+1)*10)
                check = progress_stat.write(str((i+1)*10)+"%")
                ts.sleep(1)
elif opt == "Full stack-python":
    with st.form("FSP",clear_on_submit = True,border = True):
        st.subheader("Full stack-python registration form")
        f_n,l_n = st.columns(2)
        f_n.text_input("First Name")
        l_n.text_input("Last Name")
        st.text_input("Email address")
        age,course = st.columns(2)
        age.text_input("Age")
        course.text_input("Current Studies")
        st.slider("Rate Your Coding knowledge",min_value = 15)
        
        img = st.file_uploader("Upload your ID proof",type = ["png","jpg","jpeg"],accept_multiple_files= False)
        if img is not None:
            for i in img:
                st.image(i,width=500)
        st.checkbox("Not a robot",value = False)
        status = st.form_submit_button("Finished")
        if status:
            bar = st.progress(0)
            progress_stat = st.empty()
            for i in range(10):
                bar.progress((i+1)*10)
                check = progress_stat.write(str((i+1)*10)+"%")
                ts.sleep(1)
else:
    with st.form("ML",clear_on_submit = True,border = True):
        st.subheader("Machine Learning registration form")
        f_n,l_n = st.columns(2)
        f_n.text_input("First Name")
        l_n.text_input("Last Name")
        st.text_input("Email address")
        age,course = st.columns(2)
        age.text_input("Age")
        course.text_input("Current Studies")
        st.slider("Rate Your Coding knowledge",min_value = 15)
        
        img = st.file_uploader("Upload your ID proof",type = ["png","jpg","jpeg"],accept_multiple_files= False)
        if img is not None:
            for i in img:
                st.image(i,width=500)
        st.checkbox("Not a robot",value = False)
        status = st.form_submit_button("Submit")
        if status:
            bar = st.progress(0)
            progress_stat = st.empty()
            for i in range(10):
                bar.progress((i+1)*10)
                check = progress_stat.write(str((i+1)*10)+"%")
                ts.sleep(1)

