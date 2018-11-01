import main as parse_cdp_neighbors
from draw_network_graph import *
a={}
with open('sw1_sh_cdp_neighbors.txt') as f:
    for stroki in f:
        try:
            a.update(parse_cdp_neighbors(stroki))
        except:
            pass
        draw_topology(a)
    

