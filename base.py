#!/usr/bin/env python

import networkx as nx
import random
import matplotlib.pyplot as plt
import json
import numpy as np
import math
import sys

class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def synthetic_generation(input_file, output_file, max_steps=20, nb_random_walks=200, k_index=0.001, drawing=False, key=0):
    
    # loading file
    G = nx.read_edgelist(input_file, create_using=nx.Graph(), nodetype = int)
    
    # Initialize the synthetic network
    if (max_steps != 0 and nb_random_walks != 0):
        S = nx.Graph()
        # Conduct the random walk
        for i in range(nb_random_walks):
            current_node = random.choice(list(G.nodes))
            for j in range(max_steps):
                neighbors = list(G.neighbors(current_node)) # Get the neighbors of the current node
                if not neighbors: # If there are no neighbors, stop the random walk
                    break
                next_node = random.choice(neighbors) # Choose the next node from the neighbors
                S.add_edge(current_node, next_node) # Add an edge between the current and next node to the synthetic network
                current_node = next_node # Update the current node
    else:
        S = G
    
    k = k_index/math.sqrt(len(list(S.nodes))) # Optimal distance between nodes. Increase this value to move nodes farther apart.
    
    sp = nx.spring_layout(S, dim=2, k=k) # 2-dims spring layout for drawing
    sp_3 = nx.spring_layout(S, dim=3, k=k) # 3-dims for 3D representation

    if (drawing == 'true' or drawing == 'True'):
        nx.draw_networkx(S, pos=sp, with_labels=False, node_size = 10)
        print("\n\nQuite drawing for the script to end\n\n")
        plt.show()
        
    # get list of nodes and list of edges
    list_nodes_g = list(S.nodes)
    list_edges_g = list(S.edges)
    print("Generating {} nodes and {} edges \n\n".format(len(list_nodes_g), len(list_edges_g)))
    
    # build edges connections for 3D object
    list_edges_3d_coord = []
    for i in range(0, len(list_edges_g)):
        indx_0 = list_edges_g[i][0]
        indx_1 = list_edges_g[i][1]
        list_edges_3d_coord.append([sp_3[indx_0],sp_3[indx_1]])
        
    # save to
    path = output_file + "_" + "k_indx" + str(k_index) + "_" + str(key) + ".json"
    my_dict = { "nodes" : sp_3, "edges" : list_edges_3d_coord }
    formatted = json.dumps(my_dict, cls=NumpyEncoder)
    
    with open(path, 'w') as f:
        f.write(formatted)
        print("Output ready: {} \n\n".format(path))
    
    return

if __name__ == "__main__":
    synthetic_generation(
      str(sys.argv[1]),
      str(sys.argv[2]),
      int(sys.argv[3]),
      int(sys.argv[4]),
      float(sys.argv[5]),
      str(sys.argv[6]),
      int(sys.argv[7])
    )


