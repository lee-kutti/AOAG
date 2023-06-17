import sys
import os

#file = sys.argv[1]

file = "/home/kutti/KLTN/Graphs/testing/" + sys.argv[1] + ".txt"

file_context = "/home/kutti/KLTN/Graphs/testing/" + sys.argv[1] + "_context.txt"

f_context = open(file_context, 'a')

graph_file = "/home/kutti/KLTN/Graphs/testing/Whatsapp_memdump_29052023_heapdump_graph.dot"

addrs = []

with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        addrs.append(line.split()[0])

for addr in addrs:  
    command = "pypy /home/kutti/KLTN/OAGen/artFlowGraph.py Context " + graph_file + " " + addr + " -w 20 >> " + file_context
    print (command)
    os.system(command)
    # f_context.write("\n\n")