import streamlit as st
from projects import car_analysis, network_analysis, contour_analysis, price_prediction

st.set_page_config(page_title="Data Science Portfolio", layout="wide")

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Data Visualization", "Machine Learning"])

if selection == "Home":
    st.title("My Data Science Portfolio")
    st.write("""
    ## Welcome!
    
    I am a Data Science master's student. This portfolio showcases my skills and projects.
    Use the sidebar to navigate through my work.
    """)
    
    st.image("https://placehold.co/600x400?text=Portfolio+Key+Visual", caption="Showcasing Data Science Skills")

elif selection == "Data Visualization":
    viz_selection = st.sidebar.radio("Select Visualization", ["Car Analysis", "Co-Authorship Network", "Contour Analysis"])
    
    if viz_selection == "Car Analysis":
        car_analysis.app()
    elif viz_selection == "Co-Authorship Network":
        network_analysis.app()
    elif viz_selection == "Contour Analysis":
        contour_analysis.app()

elif selection == "Machine Learning":
    ml_selection = st.sidebar.radio("Select Project", ["Used Car Price Prediction"])
    
    if ml_selection == "Used Car Price Prediction":
        price_prediction.app()
