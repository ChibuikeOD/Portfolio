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
    tab1, tab2 = st.tabs(["Interactive Dashboard", "Project Report"])

    with tab1:
        st.write("""
        ### Project Overview
        This interactive dashboard provides a comprehensive analysis of automobile data, designed to uncover hidden trends between performance metrics and market value.
        
        **Targeted Analysis Feature:**
        The core functionality of this project is the **Rectangular Region Selection** tool. This feature allows for precise subset analysis:
        - **Click and Drag** to create a rectangular selection box on either scatter plot.
        - **Highlight & Isolate**: Points inside the box remain colored, instantly isolating that specific group of cars.
        - **Linked Filtering**: The selection automatically propagates to the connected chart, revealing how vehicles in that specific performance range behave across other metrics.
        
        Use this tool to investigate outliers, identify clusters, and answer specific questions like "Do heavy cars always have low MPG?" or "Are expensive cars always high-Horsepower?"
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

    with tab2:
        st.markdown("""
        ### Project Report: Interactive Vehicle Metrics Analysis
        
        #### 1. Data Source
        - **File**: `car_sample_data.csv`
        - **Context**: This dataset aggregates specifications for a wide range of automobile models. It serves as a rich source for analyzing the trade-offs between engineering constraints (weight, fuel efficiency) and market positioning (price, horsepower).
        
        #### 2. Data Cleaning & Preparation
        - **Type Safety**: Crucial columns (`Price`, `MPG`, `Weight`, `HP`) were explicitly cast to numeric types to prevent string-based sorting errors in visualization. Non-numeric values were coerced to `NaN`.
        - **Integrity Check**: Rows lacking essential metric data were removed (`dropna`) to ensure every point on the scatter plot represents a complete and valid vehicle record.
        
        #### 3. Core Interaction: Rectangular Region Selection (Brushing)
        **The primary goal of this visualization is to demonstrate Linked Brushing.**
        - **Technique**: We implemented an interval selection mechanism using `alt.selection_interval()`.
        - **Rectangular Selection**: This allows users to "paint" a rectangle over a cluster of points. This shape is intuitive for defining ranges on two axes simultaneously (e.g., "Price between $20k-$30k" AND "HP between 100-150").
        - **Visual Feedback**:
            - **Selected Points**: Retain their color coding (by Country of Origin).
            - **Unselected Points**: Fade to neutral gray (`lightgray`). This contrast draws the eye immediately to the analysis target.
        - **Linked Views**: The selection is a shared global state. A rectangle drawn on the "Horsepower vs. Price" chart instantly filters the "Weight vs. MPG" chart, allowing for multi-dimensional cross-examination.
        
        #### 4. Key Insights & Exploration
        - **The Efficiency Trade-off**: By selecting the heaviest cars (right side of Weight chart), users can instantly see they cluster at the bottom of the MPG chart, visually confirming the physics of mass and energy.
        - **Premium Performance**: Selecting the highest price bracket reveals a strong correlation with high Horsepower, but outliers exist—users can spot expensive cars with modest specs, pointing to luxury branding over raw performance.
        """)


