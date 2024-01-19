# Import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import requests

# Load the seismic data from the NHSM API
url = "https://api.nhsm.gov/seismic_data"
response = requests.get(url)
data = pd.read_csv(response.text)

# Preprocess the data (e.g., handle missing values, normalize features)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop("label", axis=1), data["label"], test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
