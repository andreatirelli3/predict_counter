import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# Convert the list to a Pandas DataFrame
df = pd.DataFrame([2384, 2393, 2396, 2410, 2424], columns=['value'])

# Fit an ARIMA model to the data
model = ARIMA(df, order=(1,0,0))  # p=1, d=0, q=0
model_fit = model.fit()

# Make a prediction for the next value in the sequence
next_value = model_fit.forecast()[0]
print(f"ARIMA prediction: {next_value:.2f}")
