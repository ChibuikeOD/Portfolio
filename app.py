import streamlit as st
from projects import car_analysis, network_analysis, contour_analysis, price_prediction

st.set_page_config(page_title="Data Science Portfolio", layout="wide")

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Data Visualization", "Machine Learning"])

if selection == "Home":
    # Custom CSS for styling
    st.markdown("""
        <style>
        .big-font {
            font-size:50px !important;
            font-weight: bold;
            background: linear-gradient(to right, #FF4B4B, #FF9068);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subheader-font {
            font-size:20px !important;
            font-style: italic;
            color: #555;
        }
        .card {
            padding: 20px;
            border-radius: 10px;
            background-color: #f0f2f6;
            margin-bottom: 20px;
            transition: transform 0.2s; 
        }
        .card:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)

    # Hero Section
    st.markdown('<p class="big-font">Hello, I\'m Chibuike.</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader-font">Turning complex data into compelling stories and actionable insights.</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Skills Section
    st.header("🛠️ Tech Stack & Skills")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Language", value="Python 🐍")
    with col2:
        st.metric(label="Visualization", value="Altair/D3 📊")
    with col3:
        st.metric(label="Framework", value="Streamlit ⚡")
    with col4:
        st.metric(label="Domain", value="ML & AI 🤖")
        
    st.markdown("---")
    
    # Project Highlights
    st.header("🚀 Featured Projects")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Interactive Vehicle Analysis**\n\nDeep dive into car metrics with linked brushing and filtering visualizations.")
    with c2:
        st.info("**Co-Authorship Network**\n\nExplore academic collaborations through interactive force-directed graphs.")
        
    c3, c4 = st.columns(2)
    with c3:
        st.info("**Medical Contour Analysis**\n\nVisualize CT scan data with customizable density contour maps.")
    with c4:
        st.success("**Used Car Price Prediction**\n\nMachine Learning model deployed for real-time price estimation.")

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
