from sklearn.linear_model import LinearRegression

# Define the sequence
sequence = [2384, 2393, 2396, 2410, 2424]

# Create the dataset for linear regression
X = [[i] for i in range(len(sequence))]
Y = sequence

# Fit the linear regression model
model = LinearRegression()
model.fit(X, Y)

# Predict the next value in the sequence
next_position = len(sequence)
next_value = model.predict([[next_position]])[0]

print("Next value in the sequence:", next_value)
