import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Convert the list to a Pandas DataFrame
df = pd.DataFrame([2384, 2393, 2396, 2410, 2424], columns=['value'])

# Split the data into training and testing sets
n_train = int(len(df) * 0.8)
train = df.iloc[:n_train, :]
test = df.iloc[n_train:, :]

# Train a linear regression model on the training set
model = LinearRegression()
model.fit(train.iloc[:, :-1], train.iloc[:, -1])

# Make a prediction for the next value in the sequence
next_value = model.predict(test.iloc[-1, :-1].values.reshape(1,-1))
print(f"Linear regression prediction: {next_value[0]:.2f}")
