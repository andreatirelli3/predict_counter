import pandas as pd
import numpy as np

# Convert the list to a Pandas DataFrame
df = pd.DataFrame([2384, 2393, 2396, 2410, 2424], columns=['value'])

# Create a transition matrix based on the sequence data
states = np.unique(df['value'])
n_states = len(states)
transitions = np.zeros((n_states, n_states))
for i in range(n_states-1):
    current_state = states[i]
    next_state = states[i+1]
    current_count = len(df[df['value']==current_state])
    next_count = len(df[df['value']==next_state])
    transitions[i, i+1] = next_count / current_count

# Calculate the probability of each state being the next in the sequence
current_state = df.iloc[-1, -1]
probabilities = transitions[current_state, :]
next_state = np.argmax(probabilities)
next_value = states[next_state]
print(f"Markov Chain prediction: {next_value:.2f}")
