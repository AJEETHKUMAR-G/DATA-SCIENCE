import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#st.sidebar.write("This is a sidebar")
opt = st.sidebar.radio("Select any Graph",options = ("Bar","Hbar","Line"))
if opt =="Line":
    st.header("Line chart")
    fig = plt.figure()
    x = np.linspace(0,10,100)
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x),"--")
    st.write(fig)
elif opt == "Bar":
    st.header("Bar chart")
    fig = plt.figure()
    x = np.array([1,3,2,5,7,33])
    y = np.array([22,33,44,55,11,21])
    plt.bar(x,y)
    st.write(fig)
else:
    st.header("Barh chart")
    fig = plt.figure()
    x = np.array([1,3,2,5,7,33])
    y = np.array([22,33,44,55,11,21])
    plt.barh(x,y)
    st.write(fig)

