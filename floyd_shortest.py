import matplotlib.pyplot as plt
import networkx as nx

import time

from matplotlib import pyplot as plt

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

G = nx.DiGraph()

G.add_nodes_from([0,1,2,3])
G.add_edges_from([(0,1, {'weight': 8}),
                  (0,3, {'weight': 1}),
                  (1,2, {'weight': 1}),
                  (2,0, {'weight': 4}),
                  (3,1, {'weight': 2}),
                  (3,2, {'weight': 9}),
                  ])

L = nx.spring_layout(G)


print(G.number_of_nodes())
print(G.number_of_edges())


n=G.number_of_nodes()

nx.draw(G, pos = L, with_labels=True, font_weight="bold")
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, L)

print(edge_labels)

#G = nx.convert_node_labels_to_integers(G, first_label=0, ordering='default', label_attribute=None)

g = [[0,8,float('inf'),1],
     [float('inf'),0,1,float('inf')],
     [4,float('inf'),0,float('inf')],
     [float('inf'),2,9,0]]

sp = [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] > g[i][k]+g[k][j]:
                g[i][j] = g[i][k]+g[k][j]
                sp[i][j] = k

print(g)
print(sp)

start = 0
end = 1

time.sleep(0.75)


if sp[start][end]==0:
    nx.draw_networkx_edges(G, L, edgelist=[(start,end)], width=8, edge_color='b', alpha=0.2)
    plt.pause(1e-17)
else:
    nx.draw_networkx_edges(G, L, edgelist=[(start,sp[start][end])], width=8, edge_color='b', alpha=0.2)
    plt.pause(1e-17)
    time.sleep(5)
    nx.draw_networkx_edges(G, L, edgelist=[(sp[start][end], end)], width=8, edge_color='b', alpha=0.2)
    plt.pause(1e-17)


plt.show()









