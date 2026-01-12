import streamlit as st
import streamlit.components.v1 as components
import os
import json

def app():
    st.header("Co-Authorship Network Analysis")
    st.write("""
    ### Project Overview
    An interactive D3.js force-directed graph visualization showing co-authorship relationships from Scopus publication data.
    
    **Features:**
    - **Force-Directed Layout**: Dynamic network visualization.
    - **Interactive Controls**: Adjust force parameters (charge, collision, gravity).
    - **Hover Effects**: Highlight authors from the same country.
    - **Click Tooltips**: View detailed author stats.
    """)

    tab1, tab2 = st.tabs(["Network Graph", "Project Report"])

    with tab1:
        # Paths
        base_path = os.path.dirname(os.path.dirname(__file__))
        project_path = os.path.join(base_path, 'projects', 'MAssignment3')
        html_path = os.path.join(project_path, 'index.html')
        json_path = os.path.join(project_path, 'author_network.json')
    
        # Load content
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            with open(json_path, 'r', encoding='utf-8') as f:
                network_data = json.load(f)
                
        except FileNotFoundError as e:
            st.error(f"Could not load project files: {e}")
            return
    
        # Inject JSON data into HTML
        json_str = json.dumps(network_data)
        
        # Script to inject data
        # replacement logic remains the same
        
        # We need to replace `d3.json('author_network.json')` with `Promise.resolve(JSON_DATA)`
        replacement_call = f"Promise.resolve({json_str})"
        
        modified_html = html_content.replace(
            "d3.json('author_network.json')", 
            replacement_call
        )
        
        # Render
        components.html(modified_html, height=850, scrolling=True)

    with tab2:
        st.markdown("""
        ### Project Report: Co-Authorship Network Analysis
        
        #### 1. Data Source
        - **Data**: Scopus Publication Data (`author_network.json`).
        - **Description**: The dataset represents authors as nodes and their collaborative publications as links.
        
        #### 2. Visualization Technique
        - **Library**: **D3.js** (Data-Driven Documents).
        - **Layout**: **Force-Directed Graph**. This algorithm simulates physical forces to arrange the graph:
            - **Charge**: Nodes repel each other to prevent overlap.
            - **Gravity**: Pulls nodes toward the center to keep the graph coherent.
            - **Collision Detection**: Prevents nodes from overlapping visually.
        
        #### 3. Interactive Features
        - **Dynamic Controls**: Users can adjust force parameters (Collision Radius, Charge Strength) in real-time to see how the network structure changes.
        - **Country Grouping**: The visualization colors nodes/authors by their affiliated country, allowing users to spot international clusters.
        - **Hover & Click**: Tooltips provide detailed statistics (number of publications, citations) for each author.
        """)

