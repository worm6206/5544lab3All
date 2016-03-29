import simplejson as json
import sys
import numpy as np
import itertools

def build_dict(seq,key):
    return dict((d[key],dict(d,index = index)) for (index,d) in enumerate(seq))

ego_nodes = ["0","107","348","414","686","698","1684","1912","3437","3980"]

result = {}

for ego in ego_nodes:

    circles_f = ("facebook/facebook/%s.circles"%ego)

    edges_f = ("facebook/facebook/%s.edges"%ego)



    c = 2
    lines = [line.strip() for line in open(circles_f)]
    my_list = range(len(lines))
    pairs = [list(x) for x in itertools.combinations(my_list,2)]

    for pair in pairs:
        nodes = [];
        links = [];
        nodes.append({"name":int(ego),"group":1})
        circles = [lines[i] for i in pair]
        for line in circles:
            for n in line.split()[1:]:
                if {"name":int(n),"group":1} not in nodes:
                    nodes.append({"name":int(n),"group":1})
                    links.append({"source":0,"target":(len(nodes)-1)})
            c = c+1

        for line in open(edges_f):
            s = line.split();
            if ({"name":int(s[0]),"group":1} in nodes) and ({"name":int(s[1]),"group":1} in nodes):
                    ind1 = nodes.index({"name":int(s[0]),"group":1})
                    ind2 = nodes.index({"name":int(s[1]),"group":1})
                    links.append({"source":ind1,"target":ind2})


        c = 2
        for line in circles:
            for n in line.split()[1:]:
                
                if {"name":int(n),"group":1} in nodes:
                    nodes[nodes.index({"name":int(n),"group":1})]["group"] = c
                    
                else:
                    index = next(index for (index, d) in enumerate(nodes) if d["name"] == int(n))
                    nodes[index]["group"]= 1
                    
            c = c+1
        result["nodes"]=nodes
        result["links"] = links
        f = open("data/%s-%d-%d.json"%(ego,pair[0],pair[1]),'w')
        f.write(json.dumps(result))
    print ego


"""
info_by_name = build_dict(nodes,key="name")


for line in open(edges_f):
    n = line.split()
    source = info_by_name[int(n[0])]["index"]
    target = info_by_name[int(n[1])]["index"]
    links.append({"source":source,"target":target})
"""

    


    
