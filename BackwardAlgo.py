def viterbi(obs, states, start_p, trans_p, emit_p):
    V=[{}]
    for i in states:
        V[0][i]=start_p[i]*emit_p[i][obs[0]]
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
        for i in dptable(V):
            print(i)
        opt=[]
        for j in V:
            for x,y in j.items():
                if j[x]==max(j.values()):
                    opt.append(x)
    #the highest probability
    h=max(V[-1].values())
    print('The steps of states are '+' '.join(opt)+' with highest probability of %s'%h)
    #it prints a table of steps from dictionary

def dptable(V):
    yield " ".join(("%10d" % i) for i in range(len(V)))
    for y in V[0]:
        yield "%.7s: " % y+" ".join("%.7s" % ("%f" % v[y]) for v in V)

#Data
states = ('Hot', 'Cold')
end_state = 'E'

observations = ('1', '2', '3')

start_probability = {'Hot': 0.8, 'Cold': 0.2}

transition_probability = {
    'Hot': {'Hot': 0.6, 'Cold': 0.3, 'E': 0.1},
    'Cold': {'Hot': 0.4, 'Cold': 0.5,'E': 0.1}
}

emission_probability = {
    'Hot': {'1': 0.2, '2': 0.4, '3': 0.4},
    'Cold': {'1': 0.5, '2': 0.4, '3': 0.1},
}


viterbi(
    observations,
    states,
    start_probability,
    transition_probability,
    emission_probability
)