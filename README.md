# Data Science Portfolio

This is a Streamlit-based portfolio application designed to showcase data science projects. 
It currently includes:
- **Car Data Analysis**: An interactive exploration of vehicle performance metrics.

## How to Run
1. Ensure you have the required dependencies:
   ```bash
   pip install streamlit pandas altair
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

## How to Add a New Project
To add a new project to this portfolio, follow these 3 simple steps:

### 1. Create the Project File
Create a new Python file in the `projects/` folder (e.g., `projects/my_new_project.py`).
Inside this file, define an `app()` function that contains your Streamlit code.

**Example `projects/my_new_project.py`:**
```python
import streamlit as st
import pandas as pd

def app():
    st.header("My New Project")
    st.write("This is a new project added to the portfolio.")
    # Your visualization code here
```

### 2. Update `app.py`
Import your new module in `app.py` and add it to the navigation logic.

**In `app.py`:**
```python
# 1. Import the module
from projects import car_analysis, my_new_project  # <--- Add your import

# ... existing code ...

# 2. Add to radio button options
selection = st.sidebar.radio("Go to", ["Home", "Car Analysis", "My New Project"]) # <--- Add name here

# ... existing code ...

# 3. Add generic handling or specific elif
elif selection == "Car Analysis":
    car_analysis.app()
elif selection == "My New Project": # <--- Add condition
    my_new_project.app()
```

### 3. Add Data (Optional)
If your project uses data, place the CSV/Excel files in the `data/` directory and refer to them in your code.
