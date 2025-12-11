import pandas as aju
import pickle
import streamlit as st
import numpy as np

pickle_in = pickle.open('classifier.pkl',rb)
classifier = pickle.load(pickle_in)