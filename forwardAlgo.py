states = ('Healthy', 'Fever')
end_state = 'E'

observations = ('normal', 'cold', 'dizzy')

start_probability = {'Healthy': 0.6, 'Fever': 0.4}

transition_probability = {
    'Healthy': {'Healthy': 0.69, 'Fever': 0.3, 'E': 0.01},
    'Fever': {'Healthy': 0.4, 'Fever': 0.59, 'E': 0.01},
}

emission_probability = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
}

# One more Example:

# states = ('Rainy', 'Sunny')
# end_state = 'E'
#
# observations = ('walk', 'shop', 'clean')
#
# start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
#
# transition_probability = {
#     'Rainy': {'Rainy': 0.69, 'Sunny': 0.3, 'E': 0.01},
#     'Sunny': {'Rainy': 0.4, 'Sunny': 0.59,'E': 0.01},
# }
#
# emission_probability = {
#     'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
#     'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
# }


def fwd_bkw(x, states, start_probability, a, e, end_state):
    L = len(x)

    fwd = []
    f_prev = {}
    # forward part of the algorithm
    for i, x_i in enumerate(x):
        f_curr = {}
        for st in states:
            if i == 0:
                # base case for the forward part
                prev_f_sum = start_probability[st]
            else:
                prev_f_sum = sum(f_prev[k] * transition_probability[k][st] for k in states)

            f_curr[st] = emission_probability[st][x_i] * prev_f_sum

        fwd.append(f_curr)
        f_prev = f_curr

    print(list(f_curr[k] * transition_probability[k][end_state] for k in states))
    p_fwd = sum(f_curr[k] * transition_probability[k][end_state] for k in states)

    print(p_fwd)
    return fwd


def example():
    return fwd_bkw(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability,
                   end_state)

print(example())