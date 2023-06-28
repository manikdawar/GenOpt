from utils import *

def initial_state_bipartition(G):
    length = len(G.nodes)
    state = [random.randint(0, 1) for _ in range(length)]
    return state


def mutate_bipartition(state, flip_prob = 0.5):
    new_state = copy.deepcopy(state)
    for idx in range(len(new_state)):
        if random.random() < flip_prob:
            new_state[idx] = 1 - new_state[idx]
    return new_state


def fitness_bipartition(G, state):
    nodes = list(G.nodes)
    delta = max([G.degree(node) for node in nodes])
    A = 0.25 * min(2*delta, len(nodes))

    fitness = 0

    for u, v in G.edges():
        uvar = 2*state[nodes.index(u)] - 1
        vvar = 2*state[nodes.index(v)] - 1
        fitness += 0.5*(1 - uvar * vvar)

    ising_state = [A*(2*state[i] - 1) for i in range(len(state))]
    inequality = sum(ising_state)**2
    fitness += inequality

    return fitness


def simulated_annealing(G, initial_state, max_iter = 2000, T=100, alpha=0.99):

    state = initial_state
    fitness = fitness_bipartition(G, state)
    best_state = state
    best_fitness = fitness
    states, fitnesses = [], []
    for _ in range(max_iter):
        new_state = mutate_bipartition(state)
        new_fitness = fitness_bipartition(G, new_state)
        if new_fitness < fitness:
            state = new_state
            fitness = new_fitness
            states.append(state)
            fitnesses.append(fitness)
            if new_fitness < best_fitness:
                best_state = new_state
                best_fitness = new_fitness
        else:
            if random.random() < math.exp((fitness - new_fitness)/T):
                state = new_state
                fitness = new_fitness
                states.append(state)
                fitnesses.append(fitness)
        T *= alpha

    simulated_annealing.states = states
    simulated_annealing.fitnesses = fitnesses

    return best_state, best_fitness    





