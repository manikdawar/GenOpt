import random, math
import numpy as np
import networkx as nx
import copy
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


def community_output_graph(G, comms, title, pos):
    
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

    # Sort colors by hue, saturation, value and name.
    by_hsv = sorted((
        tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                    for name, color in colors.items())

    colours = [name for hsv, name in by_hsv]
    colours = ['tab:'+colour for colour in colours]
    cchoices = [colour for colour in colours]
  
    clength = len(comms)
    i = -1

    while True:
        if i > clength - 2:
            break
        if len(cchoices) > 0:
            choice = random.choice(cchoices)
            cchoices.remove(choice)
        else:
            break
        i+=1
        try:
            nx.draw_networkx_nodes(G, pos, nodelist = comms[i], node_color=choice)

        except ValueError:
            i-=1
            continue
        

    plt.title(title)
    nx.draw_networkx_edges(G, pos)
    _ = nx.draw_networkx_labels(G, pos)


def bipartition_to_set(G, partition):

    nodes = list(G.nodes)
    comm1, comm2 = [], []

    for classification in range(len(partition)): 
        if partition[classification] == 1:
            comm1.append(nodes[classification])
        else:
            comm2.append(nodes[classification])
    
    comms = [comm1, comm2]
    return comms
