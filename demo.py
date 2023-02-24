import numpy as np

data = [2384, 2393, 2396, 2410, 2424]


def distance(data):
    # Calculate the distance between each value
    differences = []
    for i in range(len(data) - 1):
        diff = data[i+1] - data[i]
        differences.append(diff)

    # AVG distance
    return sum(differences) / len(differences)

# print("Average distance:", avg_distance)


def deviation(data):
    # Calculate the standard deviation
    values = np.array(data)
    return np.std(values)

# print("Standard deviation:", std_deviation)


def predict_next_counter(data):
    # Make a prediction for the next value based on the linear trend assumption
    last_value = data[-1]
    predicted_value = last_value + distance(data)
    print("Predicted value based on linear trend:", predicted_value)

    # Compare the predicted value to the actual next value
    actual_value = 2471
    if actual_value == predicted_value:
        print("The predicted value is equal to the actual value.")
    elif actual_value > predicted_value:
        if actual_value - predicted_value > deviation(data):
            error_percentage = (actual_value - predicted_value) / actual_value * 100
            print(f"The actual value is {error_percentage:.2f}% higher than the predicted value.")
        else:
            print("The actual value is within the standard deviation range of the predicted value.")
    else:
        if predicted_value - actual_value > deviation(data):
            error_percentage = (predicted_value - actual_value) / actual_value * 100
            print(f"The actual value is {error_percentage:.2f}% lower than the predicted value.")
        else:
            print("The actual value is within the standard deviation range of the predicted value.")
