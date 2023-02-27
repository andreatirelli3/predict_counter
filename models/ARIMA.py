import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime

# Define the sequence
sequence = [2384, 2393, 2396, 2410, 2424]

# Convert the sequence to a pandas DataFrame with a date/time index
now = datetime.now()
date_index = pd.date_range(start=now.strftime("%Y-%m-%d"), periods=len(sequence), freq='D')
df = pd.DataFrame(sequence, columns=['value'], index=date_index)

# Fit the ARIMA model
model = ARIMA(df['value'], order=(1, 1, 0))
model_fit = model.fit()

# Predict the next value in the sequence
next_value = model_fit.forecast()[0]

print("Next value in the sequence:", next_value)
