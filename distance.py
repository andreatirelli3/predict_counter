# values = [2333, 2338, 2348, 2357, 2361, 2372, 2384, 2393, 2396, 2410]

half_values = [2372, 2384, 2393, 2396, 2410]

# differences = []
# for i in range(len(values) - 1):
#     diff = values[i+1] - values[i]
#     differences.append(diff)

half_differences = []
for i in range(len(half_values) - 1):
    diff = half_values[i+1] - half_values[i]
    half_differences.append(diff)

# avg_distance = sum(differences) / len(differences)
avg_half_distance = sum(half_differences) / len(half_differences)
# print("Average distance:", avg_distance)
print("Average half distance:", avg_half_distance)