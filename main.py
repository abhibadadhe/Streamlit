import numpy as np
import pandas as pd
import streamlit as st

st.title("Hello Everyone you are Welcome to the Session!!!!")
st.write("We are learning power bi python and other latest technologies")

data=pd.DataFrame({
    'c1':[10,20,30,40,50],
    'c2':['A','B','C','D','E']
})

st.write("Data is given below:")
st.write(data)

chart_data=pd.DataFrame(
    np.random.randn(20,4),columns=['P','Q','R','S']
)

st.bar_chart(chart_data)