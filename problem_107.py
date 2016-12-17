#!/usr/bin/env python3

#https://projecteuler.net/problem=107
#https://en.wikipedia.org/wiki/Prim's_algorithm

def get_network_cost(network):
    ans = 0
    for node in network:
        for edge in node[1]:
            if edge != '-':
                ans += int(edge)
    return ans//2

def select_cheapest_edge(network, nodes):
    available_edges = [e for e in network if e[0] in nodes]
    node = None
    edge = None
    for options in available_edges:
        for idx, cost in [(i, c) for i, c in enumerate(options[1]) if i not in nodes]:
            if cost != '-' and (edge == None or int(cost) < edge):
                node = idx
                edge = int(cost)
    return node, edge

network = []
with open("data/p107_network.txt") as f:
    for line in enumerate(f):
        network.append((line[0], line[1].rstrip().split(",")))

total_cost = get_network_cost(network)
network_cost = 0

nodes = [0]
ans = select_cheapest_edge(network, nodes)
while (ans[0] != None):
    nodes.append(ans[0])
    network_cost += ans[1]
    ans = select_cheapest_edge(network, nodes)

print(total_cost-network_cost)

