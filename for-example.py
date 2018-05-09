states = ('T', 'F')
end_state = 'E'

observations = ('20 BPM', '30 BPM', '40 BPM')

start_probability = {'T': 0.4, 'F': 0.6}

transition_probability = {
    'T': {'T': 0.3, 'F': 0.2, 'E': 0.5},
    'F': {'T': 0.5, 'F': 0.2, 'E': 0.3},
}

emission_probability = {
    'T': {'20 BPM': 0.5, '30 BPM': 0.3, '40 BPM': 0.2},
    'F': {'20 BPM': 0.2, '30 BPM': 0.1, '40 BPM': 0.7},
}


# def example():
#     return fwd_bkw(observations,
#                    states,
#                    start_probability,
#                    transition_probability,
#                    emission_probability,
#                    end_state)

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
