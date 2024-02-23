import streamlit as st

import numpy as np
import pandas as pd

st.markdown(
    """# This is a header
## This is a sub header
This is text"""
)

df = pd.DataFrame(
    {"first column": list(range(1, 11)), "second column": list(range(1, 11))}
)

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider("Select a line count", 1, 10, 3)
head_df = df.head(line_count)

st.dataframe(head_df)

# creating multiple sliders.
