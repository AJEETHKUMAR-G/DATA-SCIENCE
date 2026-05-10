                                        #STREAMLIT
#It is a python framework used for developing web application especially for DATA SCIENCE, AI, MACHINE LEARNING 
#Advantage: 
        #No HTML,CSS,JS
        #Safe and Secure
        #Easy to deploy
        #Compatible with scikit, keras, tensorflow, numpy
        #Maximize devlopment speed

import streamlit as st

import pandas as pd

#To start streamlit "streamlit run main.py" command is used

st.markdown(""" 
<style>
    .stDeployButton{
            visibility:hidden}
</style>""",unsafe_allow_html=True)

st.title("Hi! Welcome to streamlit")
st.subheader("I'm used to develop web application")
st.header("Advantages")
st.text("Of StreamLit:")
st.text("""   
        HTML,CSS,JS
        Safe and Secure
        Easy to deploy
        Compatible with scikit, keras, tensorflow, numpy
        Maximize devlopment speed""")

# "Markdown is similar to html tags used"
#https://www.markdownguide.org/cheat-sheet/

st.markdown("**Bold**")
st.markdown("*Italic*")
st.markdown("# H1 Tag")
st.markdown("## H2 Tag")
st.markdown("### H3 Tag")

st.markdown("1. pubg ") #Ordered List
st.markdown("2. football")

st.markdown("- Kamla") # Unordered list
st.markdown("- Bike")

st.markdown("> Blockquote")
st.markdown("---") #horizontal line

st.markdown("[Youtube](https://youtube.com)") #link
st.markdown(" ![Myimage](https://m.media-amazon.com/images/I/61iqOgq84yL._AC_UF894,1000_QL80_.jpg)") #image

st.markdown("---")

st.caption("Hi! here is the caption") #caption

# "Latex" is a mathematical tool for printing math symbols
# https://katex.org/docs/supported.html
st.latex(r"\begin{pmatrix}a & b & e\\c & d & f\end{pmatrix}")
st.latex(r"\begin{bmatrix}q & w\\e & r\end{bmatrix}")

json = {"Name":"Ajeeth","age":12,"work":"Data scientist"}
st.json(json)

code = """
a = int(input("Enter the value"))
def writing(a):
    print(a)
#function calling
writing(a)
"""
st.code(code,language = "python")

st.metric(label="wind",value="120ms⁻¹",delta = "-1.4ms⁻¹")


df = pd.DataFrame({"Name":["aju","krish","ronaldo"],"Age":[1,2,3]})
st.table(df)
st.dataframe(df) # can sort the table as per the field


st.image("krishna.jpg",caption="Radhe Krishna",width=400)
st.audio("satranga.mp3")
st.video("krish.mp4")

food = st.checkbox("Non veg")
if food:
    list = ["Chicken fried rice",'Mutton soup',"Fish curry",'Kola balls']
    for i in range(len(list)):
        st.write(list[i])
else:
    st.write("Vera hotel po da")

def change():
    print(st.session_state.checker)
st.checkbox("Veg",value=True,on_change=change,key="checker")
rad = st.radio("Which food is your favorite",options=("dosa","idly","poori"))
#print(rad)

def btn_change():
    print("form is submitted")
btn = st.button("Submit",on_click=btn_change)

select = st.selectbox("Favorite car",options=("porsche","audi","ferrari"))
#print(select)

mul = st.multiselect("Fav col",options = ("black","green","yellow"))
st.write(mul)