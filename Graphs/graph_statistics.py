import networkx as nx
import os
import sys
import time
import pygraphviz as pgv
from statistics import mean
import random
import community.community_louvain as cl
from csv import writer

path = "/home/kutti/KLTN/Graphs/" + sys.argv[1]

graph_filenames = [path + "/" + file for file in os.listdir(path)]

num_nodes_list = []
num_edges_list = []
isolated_list = []
avg_deg_list = []
avg_path_len_list = []
wcc_list = []
scc_list = []
avg_bwness_cen_list = []
net_dmeter_list = []
comm_list = []
avg_clus_coeff_list = []
name_list = []

def fetch_hugest_subgraph(graph_):
  Gcc = max(nx.connected_components(graph_), key = len)
  giantC = graph_.subgraph(Gcc)
  return giantC

def write_shortest_paths(graph_, n_samples = 2000):
  component_ = fetch_hugest_subgraph(graph_)
  nodes = component_.nodes()
  lengths = []
  for _ in range(n_samples):
    n1, n2 = random.choices(list(nodes), k = 2)
    length = nx.shortest_path_length(component_, source = n1, target = n2)
    lengths.append(length)
  print("Number of nodes: ", len(nodes), ", shortest path mean: ", mean(lengths))
  avg_path_len_list.append(mean(lengths))

def write_network_diameter (graph_):
  component_ = fetch_hugest_subgraph(graph_)
  diameter = nx.approximation.diameter(component_)
  print ("Network diameter: ", diameter)
  net_dmeter_list.append(diameter)

def write_communities(graph_):
  result = cl.best_partition(graph_)
  communities = len(set(result.values()))
  print ("Total louvain communities: ", communities)
  comm_list.append(communities)

def write_average_clustering_coefficent(graph_):
  clus_coeff = nx.average_clustering(graph_)
  print ("Average clustering coefficient: ", clus_coeff)
  avg_clus_coeff_list.append(clus_coeff)

def print_mean_statistics():
  print ("Mean diameter: ", mean(net_dmeter_list))
  print ("Mean scc count: ", mean(scc_list))
  print ("Mean wcc count: ", mean(wcc_list))
  print ("Mean number of nodes: ", mean(num_nodes_list))
  print ("Mean number of edges: ", mean(num_edges_list))
  print ("Mean average path length: ", mean(avg_path_len_list))
  print ("Mean isolated nodes ratio: ", mean(isolated_list))
  print ("Mean average degree: ", mean(avg_deg_list))
  print ("Mean community count: ", mean(comm_list))
  print ("Mean clustering coefficient: ", mean(avg_clus_coeff_list))
  print ("Mean betweenness centrality: ", mean(avg_bwness_cen_list))

  if len(net_dmeter_list) == len(scc_list) == len(num_nodes_list) == len(avg_path_len_list) == len(isolated_list) == len(avg_deg_list) == len(comm_list) == len(avg_bwness_cen_list):
    #print ("okay")
    csv_file = sys.argv[1] + ".csv"
    with open(csv_file, 'a') as f_object:
      for i in range (len(wcc_list)):
        temp_list = [name_list[i], num_nodes_list[i], num_edges_list[i], avg_deg_list[i], isolated_list[i], scc_list[i], wcc_list[i], avg_path_len_list[i], net_dmeter_list[i], comm_list[i], avg_clus_coeff_list[i], avg_bwness_cen_list[i]]
        writer_object = writer(f_object)
        writer_object.writerow(temp_list)
      f_object.close()

for graph_file in graph_filenames:
  name_list.append(graph_file)
  start_time = time.time()

  G = pgv.AGraph(graph_file, strict=False, directed=False)
  Gnx = nx.nx_agraph.from_agraph(G)

  SCC = nx.number_strongly_connected_components(Gnx)
  print ("Strongly Connected Components: ", SCC)
  WCC = nx.number_weakly_connected_components(Gnx)
  print ("Weakly Connected Components: ", WCC)
  scc_list.append(SCC)
  wcc_list.append(WCC)

  N, E = Gnx.order(), Gnx.size()
  avg_deg = float(E) / N

  isolates = list(nx.isolates(Gnx))
  print ("Number of isolated nodes: ", len(isolates))
  isolated_ratio = float(len(isolates)) / N
  print ("% Isolated: ", isolated_ratio * 100)
  isolated_list.append(isolated_ratio)

  print ("Nodes: ", N)
  num_nodes_list.append(N)

  print ("Edges: ", E)
  num_edges_list.append(E)

  print ("Average degree: ", avg_deg)
  avg_deg_list.append(avg_deg)

  Gnx = nx.Graph(Gnx)
  s = fetch_hugest_subgraph(Gnx)
  print ("Largest connected component: ", s.order(), s.size())

  write_shortest_paths(Gnx)

  write_network_diameter(Gnx)

  write_average_clustering_coefficent(Gnx)

  write_communities(Gnx)

  betweenness_centralities = nx.betweenness_centrality(Gnx, k = 2000).values()
  avg_betweenness_centrality = mean(betweenness_centralities)
  print ("Average betweenness centrality: ", avg_betweenness_centrality)
  avg_bwness_cen_list.append(avg_betweenness_centrality)

  stop_time = time.time()
  print ("Total time taken for {} is {} seconds\n".format(graph_file, str(stop_time - start_time)))

print_mean_statistics()