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
    # We replace the d3.json call with the actual data variable to avoid local server/CORS issues
    
    # serialization of the json data
    json_str = json.dumps(network_data)
    
    # Replacement string
    # We assume standard formatting from the file we viewed: 
    # d3.json('author_network.json').then(data => {
    # and ends with });
    
    # To be robust, we can inject a variable at the top of the script and change the d3.json call
    
    # Script to inject data
    data_injection = f"const injectedData = {json_str};"
    
    # Modified HTML logic:
    # 1. Inject the data variable before the main logic
    # 2. Replace `d3.json('author_network.json').then(data => {` with `const data = injectedData; {{`
    # 3. Handle the closing `});` by replacing it with `}` or leaving it if we just wrap in a block?
    # actually d3.json(...).then(arrow) returns a promise.
    # if we change to `const data = ...; { ... }` we are good as long as we remove the .then structure.
    
    # Let's do simple string replacement since we verify the file content.
    target_start = "d3.json('author_network.json').then(data => {"
    replacement_start = f"const data = {json_str}; \n {{ " # Open a block to keep scope similar
    
    # We also need to find the matching closing brackets `});` for the `then` call.
    # In the provided file, it is on line 142: `        });`
    # Replacing unique string `        });` with `        }` might work if unique.
    # Let's try a safer approach:
    # Inject the data into a global var in the head or start of body, change `d3.json(...)` to `Promise.resolve(window.injectedData)`?
    # No, `d3.json` loads file. `Promise.resolve(data).then(...)` would preserve the structure!
    
    # BETTER APPROACH:
    # Replace `d3.json('author_network.json')` with `Promise.resolve(JSON_DATA)`
    # This keeps `.then(data => { ... })` valid!
    
    replacement_call = f"Promise.resolve({json_str})"
    
    modified_html = html_content.replace(
        "d3.json('author_network.json')", 
        replacement_call
    )
    
    # Render
    components.html(modified_html, height=850, scrolling=True)

