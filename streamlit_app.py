import streamlit as st
import pandas as pd

# Set up the Streamlit app
st.set_page_config(page_title="Streamlit App", layout="wide")
st.title("🚀 My Streamlit App")
st.write("This is a simple and responsive Streamlit app.")

# User input
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Sample Data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}
df = pd.DataFrame(data)

# Display data
st.subheader("📊 Sample Data Table")
st.dataframe(df, use_container_width=True)

# Button action
if st.sidebar.button("Submit"):
    st.success(f"✅ Hello {name}, you are {age} years old!")

# Deployment Information
st.sidebar.markdown("---")
st.sidebar.markdown("### Deployment")
st.sidebar.info("To deploy, use: `streamlit run app.py`")
