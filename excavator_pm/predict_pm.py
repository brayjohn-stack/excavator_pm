import pandas as pd
import joblib

# load trained model
model = joblib.load("models/pm_best.joblib")

# load dataset
df = pd.read_csv("data/pm_sim.csv")
X = df[['temperature', 'vibration', 'oil_pressure', 'rpm', 'operating_hours', 'ambient_temp']]

# predict failures
df['predicted_failure'] = model.predict(X)

# show first 10 predictions
print(df[['timestamp', 'predicted_failure']].head(10))
