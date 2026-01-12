import streamlit as st
import pandas as pd
import altair as alt
import os

def load_data():
    # Constructing the absolute path to the data file
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Activity-7', 'data', 'car_sample_data.csv')
    return pd.read_csv(data_path)

def app():
    st.header("Interactive Vehicle Metrics Analysis")
    st.write("""
    ### Project Overview
    This interactive visualization explores a dataset of various car models to uncover relationships between performance metrics and pricing. 
    
    **The Dataset:**
    The dataset includes specifications for various automobiles, including:
    - **Performance**: Horsepower (HP), Engine Size, Weight
    - **Efficiency**: Miles Per Gallon (MPG)
    - **Economics**: Price, Origin (Country)
    
    **Analysis:**
    Use the interactive charts below to explore these relationships. 
    - **Brush Logic**: Select a rectangular region in either chart to filter the other chart and highlighting specific data points.
    """)

    try:
        df = load_data()
    except FileNotFoundError:
        st.error("Data file not found. Please check the path.")
        return

    # Clean data
    numeric_cols = ['Price', 'MPG', 'Weight', 'HP']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    df = df.dropna(subset=numeric_cols)

    # Brushing selection
    brush = alt.selection_interval()

    # Scatter Plot 1: HP vs Price
    chart1 = alt.Chart(df).mark_circle(size=60).encode(
        x='HP',
        y='Price',
        color=alt.condition(brush, 'Country:N', alt.value('lightgray')),
        tooltip=['Model', 'Price', 'HP', 'MPG', 'Weight', 'Country']
    ).add_params(
        brush
    ).properties(
        width=400,
        height=300,
        title="Horsepower vs. Price"
    )

    # Scatter Plot 2: Weight vs MPG (Linked)
    chart2 = alt.Chart(df).mark_circle(size=60).encode(
        x='Weight',
        y='MPG',
        color=alt.condition(brush, 'Country:N', alt.value('lightgray')),
        tooltip=['Model', 'Price', 'HP', 'MPG', 'Weight', 'Country']
    ).add_params(
        brush
    ).properties(
        width=400,
        height=300,
        title="Weight vs. MPG"
    )
    
    # Display charts side by side
    charts = chart1 | chart2
    
    # Render chart
    st.altair_chart(charts, use_container_width=True)

    # Data Display
    st.subheader("Dataset Info")
    st.markdown("Use the charts above to explore the dataset. Below is the full dataset for reference.")
    st.dataframe(df)


