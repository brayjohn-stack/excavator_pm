#Excavator Project
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# create timestamps for 30 days, one reading per hour
start_time = datetime.now() - timedelta(days=30)
timestamps = [start_time + timedelta(hours=i) for i in range(30 * 24)]
np.random.seed(42)

temperature = np.random.normal(80, 5, len(timestamps))       # engine temp (°C)
vibration = np.random.normal(0.5, 0.1, len(timestamps))      # vibration level
oil_pressure = np.random.normal(50, 5, len(timestamps))      # psi
rpm = np.random.normal(1500, 200, len(timestamps))           # engine speed
operating_hours = np.arange(len(timestamps)) / 24            # total hours run
ambient_temp = np.random.normal(25, 3, len(timestamps))      # outside temp
# simulate a failure event: 1 if vibration > 0.7 or temp > 90, else 0
failure = [(1 if v > 0.7 or t > 90 else 0) for v, t in zip(vibration, temperature)]

# combine into a DataFrame
df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": temperature,
    "vibration": vibration,
    "oil_pressure": oil_pressure,
    "rpm": rpm,
    "operating_hours": operating_hours,
    "ambient_temp": ambient_temp,
    "failure": failure
})
# create data folder if it doesn't exist
import os
os.makedirs("data", exist_ok=True)

# save DataFrame to CSV
df.to_csv("data/pm_sim.csv", index=False)

print("Synthetic data saved to data/pm_sim.csv")
