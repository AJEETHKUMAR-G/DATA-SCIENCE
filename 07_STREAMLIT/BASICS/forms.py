import streamlit as st
st.markdown("<h1 style='text-align:center'>User Register form</h1>",unsafe_allow_html = True)
form = st.form("Form 1")
form.text_input("Name",max_chars = 24)
form.form_submit_button("submit")

with st.form("Form 2",clear_on_submit = True,border= True):
    c1,c2 = st.columns(2)
    course = c2.text_input("Course")
    clg = c1.text_input("College Name")
    st.text_input("Email address")
    c3,c4 = st.columns(2)
    c3.text_input("Password")
    c4.text_input("Conform Password")
    day,month,yr = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    yr.text_input("Year")
    s_stats = st.form_submit_button("submit")
    if s_stats:
        if course == "" and clg == "":
            st.warning("Fill the form properly")
        else:
            st.success("Thank you")
