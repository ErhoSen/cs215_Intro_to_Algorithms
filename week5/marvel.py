import time
import csv
from collections import defaultdict

def highest_strength(graph):
    return max((s, x, y) for x, links in graph.items() for y, s in links.items())

def make_link(G, node1, node2):
    if node1 not in G: G[node1] = defaultdict(int)
    G[node1][node2] += 1     
    if node2 not in G: G[node2] = defaultdict(int)
    G[node2][node1] += 1

def read_graph(filename):
    tsv = open(filename, "r")
    tsv1 = []
    for s in tsv.readlines():
        ch, cm_b, y = s.strip().split("\t")
        tsv1.append((ch, cm_b))
    comics = {}
    for (character, comic_book) in tsv1:
        if comic_book not in comics:
            comics[comic_book] = []
        comics[comic_book].append(character)
    G = {}
    for comic_book in comics:
        i = 1
        for character in comics[comic_book]:
            for current in comics[comic_book][i:]:
                make_link(G, character, current)
            i += 1        
    return G

start_time = time.time()
G = read_graph('file')
print highest_strength(G)
print "running time:", time.time() - start_time