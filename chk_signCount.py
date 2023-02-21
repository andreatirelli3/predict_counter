MAX_SEED = 256
MIN_SEED = 1

# use Bayesian math to check if the last and the current value are correct


def chk_signcount_flow(last, current):
    if last == current:
        return 'ERR_COUNTER_TOO_LOW'
    if last + 1 == current:
        return 'ERR_COUNTER_LINEAR_SEQUENCE'
    

# ask to the user le last and the current value
last = int(input('Enter the last value: '))
current = int(input('Enter the current value: '))
print(chk_signcount_flow(last, current))
