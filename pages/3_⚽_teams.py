import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide",
)

df = st.session_state["data"]

teams = df["Club"].value_counts().index
team = st.sidebar.selectbox("Clube", teams)
df_filtered = df[df["Club"] == team].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.header(df_filtered.iloc[0]["Club"])

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)","Contract Valid Until", "Release Clause(£)"]

# Display the dataframe with the specified columns
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", min_value=0, max_value=100, format="%d"),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", min_value=0, max_value=df_filtered["Wage(£)"].max(), format="£ %f"),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),
             })