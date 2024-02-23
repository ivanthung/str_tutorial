import streamlit as st

st.title("Counter Example")
count = 0

increment = st.button("Increment without session_state")
if increment:
    count += 1

st.write("Count = ", count)

# Initialization
if "count" not in st.session_state:
    st.session_state.count = 0

increment = st.button("Increment with session state")
if increment:
    st.session_state.count += 1

st.write("Count = ", st.session_state.count)
