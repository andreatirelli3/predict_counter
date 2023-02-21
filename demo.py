import numpy as np

data = [2384, 2393, 2396, 2410, 2424]

# Calculate the distance between each value
differences = []
for i in range(len(data) - 1):
    diff = data[i+1] - data[i]
    differences.append(diff)

avg_distance = sum(differences) / len(differences)
print("Average distance:", avg_distance)

# Calculate the standard deviation
values = np.array(data)
std_deviation = np.std(values)
print("Standard deviation:", std_deviation)

# Make a prediction for the next value based on the linear trend assumption
last_value = data[-1]
predicted_value = last_value + avg_distance
print("Predicted value based on linear trend:", predicted_value)

# Compare the predicted value to the actual next value
actual_value = 2471
if actual_value == predicted_value:
    print("The predicted value is equal to the actual value.")
elif actual_value > predicted_value:
    if actual_value - predicted_value > std_deviation:
        error_percentage = (actual_value - predicted_value) / actual_value * 100
        print(f"The actual value is {error_percentage:.2f}% higher than the predicted value.")
    else:
        print("The actual value is within the standard deviation range of the predicted value.")
else:
    if predicted_value - actual_value > std_deviation:
        error_percentage = (predicted_value - actual_value) / actual_value * 100
        print(f"The actual value is {error_percentage:.2f}% lower than the predicted value.")
    else:
        print("The actual value is within the standard deviation range of the predicted value.")
