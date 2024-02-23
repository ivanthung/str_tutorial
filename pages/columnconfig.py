import pandas as pd
import streamlit as st

# Format everything with a percentage behind it
column_config = {
    "numbers": st.column_config.NumberColumn(
        "Changed name",
        format="%.2f%%",
        min_value=0,
        max_value=10,
    )
}

data_df = pd.DataFrame(
    {
        "numbers": [1, 2, 3, 4],
    }
)

data_df_edited = st.data_editor(
    data_df,
    hide_index=True,
    column_config=column_config,
    num_rows="dynamic",
)

data_df_edited
