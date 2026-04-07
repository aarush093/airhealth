import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

data = {
    "temperature": np.random.uniform(20, 80, n),
    "vibration": np.random.uniform(0, 10, n),
    "pressure": np.random.uniform(30, 100, n),
    "runtime_hours": np.random.uniform(0, 5000, n),
    "error_code_count": np.random.randint(0, 20, n)
}

df = pd.DataFrame(data)

df["failure"] = ((df["temperature"] > 65) |
                 (df["vibration"] > 8) |
                 (df["pressure"] > 85) |
                 (df["runtime_hours"] > 4000)).astype(int)

df.to_csv("sensor_data.csv", index=False)
print("Dataset created successfully!")
print(df.head())
print(f"\nFailure cases: {df['failure'].sum()} out of {n}")
