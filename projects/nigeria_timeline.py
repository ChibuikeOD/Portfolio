import streamlit as st
import streamlit.components.v1 as components
import os
import json

def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_dataset(base_path, filename):
    file_path = os.path.join(base_path, 'Datasets', filename)
    try:
        return load_file(file_path)
    except FileNotFoundError:
        st.error(f"Could not find dataset: {filename}")
        return ""

def app():
    st.header("Nigeria Economic Timeline")
    
    # Define paths
    base_path = os.path.join(os.path.dirname(__file__), 'Nigeria-Economic-Timeline')
    
    # Load core files
    try:
        html_content = load_file(os.path.join(base_path, 'index.html'))
        css_content = load_file(os.path.join(base_path, 'styles.css'))
        js_content = load_file(os.path.join(base_path, 'app.js'))
    except FileNotFoundError as e:
        st.error(f"Error loading project files: {e}")
        return

    # Load Datasets
    # These matches the filenames in app.js CONFIG.datasets
    datasets = {
        'API_PA.NUS.FCRF_DS2_en_csv_v2_2844.csv': load_dataset(base_path, 'API_PA.NUS.FCRF_DS2_en_csv_v2_2844.csv'),
        'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_322200.csv': load_dataset(base_path, 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_322200.csv'),
        'API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_322193.csv': load_dataset(base_path, 'API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_322193.csv'),
        'API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_322058.csv': load_dataset(base_path, 'API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_322058.csv'),
        'API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_322167.csv': load_dataset(base_path, 'API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_322167.csv'),
        'API_SP.DYN.LE00.IN_DS2_en_csv_v2_321761.csv': load_dataset(base_path, 'API_SP.DYN.LE00.IN_DS2_en_csv_v2_321761.csv'),
        'API_SP.POP.TOTL_DS2_en_csv_v2_322199.csv': load_dataset(base_path, 'API_SP.POP.TOTL_DS2_en_csv_v2_322199.csv')
    }

    # Inject Data and Scripts
    # We need to modify the JS to use our injected data instead of fetch()
    
    # 1. Create a global object for data
    injected_data_script = f"""
    <script>
        window.INJECTED_DATA = {json.dumps(datasets)};
        
        // Override the fetch function to intercept calls to Datasets/
        const originalFetch = window.fetch;
        window.fetch = async (url) => {{
            if (url.includes('Datasets/')) {{
                const filename = url.split('Datasets/')[1];
                if (window.INJECTED_DATA[filename]) {{
                    return {{
                        ok: true,
                        text: async () => window.INJECTED_DATA[filename]
                    }};
                }}
            }}
            return originalFetch(url);
        }};
    </script>
    """

    # 2. Inject CSS
    css_injection = f"<style>{css_content}</style>"

    # 3. Inject JS
    js_injection = f"<script>{js_content}</script>"

    # 4. Construct final HTML
    # We strip out external script references (d3 is already in index.html, we keep it)
    # We remove the local script src="app.js" link and inject the content directly
    
    # Naive HTML processing
    final_html = html_content
    
    # Remove link to styles.css
    final_html = final_html.replace('<link rel="stylesheet" href="styles.css">', css_injection)
    
    # Remove script tag for app.js (assuming it's at the end)
    # We'll just define the global data BEFORE the existing scripts run
    
    # Actually, it's safer to reconstruct the body.
    # index.html has:
    # <script src="https://d3js.org/d3.v7.min.js"></script> -> KEEP or CDN
    # <script src="app.js"></script> -> REMOVE and Inject
    
    # Let's replace the script tag for app.js with our injected content
    # Note: app.js in index.html is INLINE inside <script> tags in the provided index.html content (Step 83).
    # Wait, looking at Step 83, index.html contains the full JS logic inside <script> tags at the bottom.
    # BUT Step 84 showed `app.js` as well.
    # Let's re-examine Step 83 (index.html).
    # Lines 53-699 seem to be the `app.js` content directly embedded or very similar.
    # Lines 1-12 match typical head. 
    # Line 11: <script src="https://d3js.org/d3.v7.min.js"></script>
    # The file listing showed `app.js` exists.
    # If index.html already has the script inline, we just need to inject the data interceptor BEFORE that script runs.
    
    # If the user provided `index.html` has the script inline (as seen in Step 83), we don't need to load `app.js` separately *unless* the user wants to use the `app.js` file instead of the inline one.
    # However, `index.html` step 83 lines 53-699 IS the logic.
    # And Step 84 `app.js` is ALSO logic. they look identical. 
    # It's likely `index.html` is self-contained OR it was a copy-paste.
    # Let's look at `index.html` again.
    # Line 10: <link rel="stylesheet" href="styles.css">
    # It does NOT have `<script src="app.js"></script>`. It has inline `<script>`.
    
    # So for `index.html`, I need to:
    # 1. Inject the `window.fetch` override script resource at the top of the body or head.
    # 2. Inject the contents of `styles.css` to replace the link tag.
    # 3. Use the `index.html` content as the base.
    
    # Wait, `index.html` (Step 83) fetches data:
    # Line 57: file: 'Datasets/API_PA.NUS.FCRF_DS2_en_csv_v2_2844.csv'
    # Line 224: const response = await fetch(dataset.file);
    
    # So my interceptor strategy is correct.
    
    # Update: I will modify the `index.html` string.
    
    # a. Inject Data Interceptor at the start of <script> (Line 53)
    parts = final_html.split('<script>')
    if len(parts) > 1:
        # parts[0] is everything before first <script>
        # but there is d3 script in head. 
        # let's be more specific. The inline script starts after d3?
        # d3 is line 11.
        # Main script is line 53.
        pass

    # Better approach:
    # Inject `injected_data_script` right before `</body>`.
    # But wait, `document.addEventListener('DOMContentLoaded', loadAllData);` is at the end.
    # `loadAllData` calls `fetch`.
    # As long as my interceptor runs before `loadAllData` fires, it's fine.
    # So injecting at the top of <body> is safest.
    
    html_soup = final_html
    
    # Inject CSS
    html_soup = html_soup.replace('<link rel="stylesheet" href="styles.css">', css_injection)
    
    # Inject Data Interceptor
    # We put it right after <body>
    html_soup = html_soup.replace('<body>', f'<body>{injected_data_script}')
    
    components.html(html_soup, height=900, scrolling=True)

if __name__ == "__main__":
    app()
