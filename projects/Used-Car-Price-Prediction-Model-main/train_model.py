import pandas as pd
import pickle
from sklearn.ensemble import ExtraTreesRegressor
# from sklearn.model_selection import train_test_split # Not strictly needed if we just train on all data for the app demo
import os

# Paths
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, 'car data.csv')
model_path = os.path.join(current_dir, 'model.pkl')

if not os.path.exists(data_path):
    print(f"Error: '{data_path}' not found.")
    print("Please add the dataset file to train the model.")
    exit()

print("Loading data...")
df = pd.read_csv(data_path)

# Preprocessing from notebook
# 'Year' -> 'Age'
df['Current_Year'] = 2024 # Fixed reference or dynamic
df['Age'] = df['Current_Year'] - df['Year']
df.drop(['Year', 'Current_Year'], axis=1, inplace=True)

# Drop Name
df.drop(['Car_Name'], axis=1, inplace=True)

# One Hot Encoding
# get_dummies(drop_first=True) avoids collinearity
final_dataset = pd.get_dummies(df, drop_first=True)

# Features and Label
X = final_dataset.iloc[:, 1:] # Features (assuming Selling_Price is col 0, check below)
# Wait, Selling_Price position depends on get_dummies column order? 
# In original DF: Selling_Price is often 2nd col.
# Let's be explicit.

target_col = 'Selling_Price'
if target_col in final_dataset.columns:
    y = final_dataset[target_col]
    X = final_dataset.drop([target_col], axis=1)
else:
    # If get_dummies messed up order? No, columns persist.
    print("Error: Target column not found.")
    exit()

print(f"Features: {X.columns.tolist()}")

# Train Model
print("Training ExtraTreesRegressor...")
model = ExtraTreesRegressor()
model.fit(X, y)

# Save
print(f"Saving model to {model_path}...")
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("Done! Model trained and saved.")
