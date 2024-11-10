import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime
import os

# Set the page configuration
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="centered",
)

repo_root = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(repo_root, "datasets", "CLEAN_FIFA23_official_data.csv")

# Load the data if it's not already loaded
if "data" not in st.session_state:
    df_data = pd.read_csv(data_path, index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year] # Filter out players with expired contracts
    df_data = df_data[df_data["Value(£)"] > 0] # Filter out players with zero value
    df_data = df_data.sort_values(by="Overall", ascending=False) # Sort by overall rating
    st.session_state["data"] = df_data # Store the dataframe in the session state

# Display the content
st.markdown("# FIFA 2023 OFFICIAL DATASET! ⚽️") 
st.sidebar.markdown("# Home 🏠\n Desenvolvido por [Asimov Academy](https://asimov.academy)")

# Create a button to open the Kaggle link
btn = st.button("Acesse os dados no Kaggle")

if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data') # Open the link in a new tab

# Display the description of the dataset
st.markdown("""
            The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. 
            The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. 
            With **over 17,000 records**, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, 
            as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.
            """)