# python autoGraph.py /benign | tee -a autoGraph_output_benign.txt
# python autoGraph.py /malware | tee -a autoGraph_output_malware.txt

import os
import sys

os.chdir("../MemDumps")
memdumps_path = os.getcwd() + sys.argv[1]

mem_heap_dict = {}

for memdump_foldername in os.listdir(memdumps_path):
    heapdump_filename = memdump_foldername + "_heapdump.out"
    mem_heap_dict.update({memdump_foldername: heapdump_filename})

print mem_heap_dict

os.chdir("../Graphs")
graphs_path = os.getcwd() + sys.argv[1]

os.chdir("../HeapDumps")
heapdumps_path = os.getcwd() + sys.argv[1]

os.chdir("../OAGen")
oagen_path = os.getcwd()

for mem, heap in mem_heap_dict.items():
    try:
        print "Starting Graph with " + heap
        graph_filename = mem + "_heapdump_graph.dot"
        command = "pypy " + oagen_path + "/artFlowGraph.py Graph " + memdumps_path + "/" + mem + " " + heapdumps_path + "/" + heap + " " + graphs_path + "/" + graph_filename
        # print (command)
        return_code = os.system(command)
        if return_code == 0:
            print "graph " + heap + " completed successfully"
        else:
            print "graph " + heap + " failed with exit code " + return_code
    except Exception as e:
        print "Exception in " + heap + ": " + str(e)