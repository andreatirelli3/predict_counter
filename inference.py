import pymc3 as pm
import numpy as np

# Define the data
data = np.array([2333, 2338, 2348, 2357, 2361, 2372, 2384, 2393, 2396, 2410])

# Define the model
with pm.Model() as model:
    mu = pm.Uniform('mu', lower=2000, upper=2500)
    sigma = pm.HalfNormal('sigma', sd=10)
    obs = pm.Normal('obs', mu=mu, sd=sigma, observed=data)

# Run the model
with model:
    trace = pm.sample(10000)

# Print the summary of the trace
pm.summary(trace)
