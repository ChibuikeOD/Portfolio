import streamlit as st
import streamlit.components.v1 as components
import os
import json

def app():
    st.header("CT Scan Contour Analysis")
    st.write("""
    ### Project Overview
    This tool visualizes **CT (Computed Tomography) scan data** by generating contour lines that represent regions of similar tissue density. 
    It helps in identifying distinct anatomical structures based on their density values.
    
    **How to Use:**
    1.  **Select Brain Scan**: Choose a DICOM file from the dropdown menu to load a different brain slice.
    2.  **Adjust Visualization**: Use the sliders below the visualization to refine the analysis.
    
    **Controls Guide:**
    -   **Bin Count**: Determines the **number of contour levels**. Increasing this value adds more detail and smoother transitions, while decreasing it simplifies the view.
    -   **Min Threshold**: Sets the **minimum density value** to display. Increasing this removes lower-density areas (like background noise or soft tissue), isolating denser structures.
    -   **Max Threshold**: Sets the **maximum density value** to display. Decreasing this focuses the visualization on a specific density range, excluding the densest materials (like bone).
    """)

    # Paths
    base_path = os.path.dirname(os.path.dirname(__file__))
    project_dir = os.path.join(base_path, 'projects', 'CIS-568-Activity-6', 'Activity 6', 'CIS-568-Activity-6')
    html_path = os.path.join(project_dir, 'activity.html')
    data_dir = os.path.join(project_dir, 'dicomData')

    try:
        # Get list of JSON files
        files = [f for f in os.listdir(data_dir) if f.endswith('.json')]
        files.sort()
        
        # Streamlit Selector
        selected_file = st.selectbox("Select Brain Scan:", files, index=0)
        
        # Load HTML
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # Load Data
        data_path = os.path.join(data_dir, selected_file)
        with open(data_path, 'r', encoding='utf-8') as f:
            dicom_data = json.load(f)
            
    except Exception as e:
        st.error(f"Error loading project files: {e}")
        return

    # Serialize data
    json_str = json.dumps(dicom_data)
    
    # Modifications to HTML:
    # 1. Inject data
    # 2. Override `plotContour` to use injected data instead of fetching
    # 3. Hide the internal selector
    
    # CSS injection to hide the HTML selector
    css_injection = """
    <style>
        #files_container { display: none !important; }
        .main { gap: 0; justify-content: center; }
        .canvas { box-shadow: none; border: 1px solid #ddd; }
    </style>
    """
    html_content = html_content.replace("<head>", f"<head>{css_injection}")
    
    # JS Injection
    # We replace the `plotContour` function call or body.
    # The original script does: `plotContour(files_data[0]);` at the end.
    # And `plotContour` does `d3.json(...)`.
    
    # We will redefine `plotContour` to accept data directly or just call `drawLogic(data)`.
    # Let's see the code structure again. 
    # `plotContour(filename)` calls `d3.json` then processing logic.
    # We can replace the `d3.json` call.
    
    # We will replace `d3.json("dicomData/" + filename).then(data => {`
    # with `Promise.resolve(INJECTED_DATA).then(data => {`
    # But strictly, the `filename` argument in the function becomes irrelevant.
    
    # Actually, simpler:
    # 1. Inject `const INJECTED_DATA = ...;` at top of script.
    # 2. Replace the `d3.json(...)` line with `Promise.resolve(INJECTED_DATA).then(data => {`
    # 3. Remove the initial `plotContour(files_data[0]);` call at the bottom and call `plotContour(null)` or similar?
    # Actually, the implementation calls `plotContour` with a filename.
    # If we replace d3.json, it will use our injected data regardless of the filename arg.
    
    target_d3_call = 'd3.json("dicomData/" + filename).then(data => {'
    replacement_d3_call = f'Promise.resolve({json_str}).then(data => {{'
    
    html_content = html_content.replace(target_d3_call, replacement_d3_call)
    
    # Note: The HTML also populates a dropdown `#files`. We should suppress that or let it be hidden by CSS.
    # The script calls `plotContour(files_data[0]);` at the end. 
    # This will trigger our replaced code which uses `json_str` (the *selected* file from streamlit).
    # So `files_data[0]` passed to it doesn't matter, but it ensures the logic runs once.
    
    components.html(html_content, height=700, scrolling=True)
