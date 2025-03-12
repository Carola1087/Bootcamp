import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'columna 1': [1, 2, 3, 4],
    'columna 2': [10, 20, 30, 40]
}))