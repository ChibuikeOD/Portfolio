# Data Science Portfolio

Welcome to my Data Science Portfolio! This application is built with Streamlit and serves as a centralized hub to showcase my skills in data visualization, machine learning, and interactive web application development.

It currently features the following projects:

- **Car Data Analysis**: An interactive dashboard exploring vehicle performance metrics using Altair.
- **Co-Authorship Network**: A force-directed graph visualization of academic co-authorship using D3.js.
- **Contour Analysis**: A medical imaging tool for visualizing CT scan density contours.
- **Used Car Price Prediction**: A machine learning application that predicts car prices based on user inputs.


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
