import numpy as np
import pandas as pd
import streamlit as st

st.title("Hello All Good Evening!!!")
st.write("Here is the example of streamlit for Cloud Deployment")

data=pd.DataFrame({
    'names':['sachin','gautam','yash','om','amol'],
    'marks':[89,77,58,70,65]
})

st.write("Below table shows marks of the students:")
st.write(data)

chart_data=pd.DataFrame(np.random.randn(30,4),columns=['A','B','C','D'])
st.line_chart(chart_data)