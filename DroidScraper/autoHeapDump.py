# python autoHeapDump.py /benign >> autoHeapDump_output_benign.txt
# python autoHeapDump.py /malware >> autoHeapDump_output_malware.txt

import os
import sys

os.chdir("../MemDumps")
memdumps_path = os.getcwd() + sys.argv[1]
os.chdir("../HeapDumps")
heapdumps_path = os.getcwd() + sys.argv[1]
os.chdir("../DroidScraper")
droidscraper_path = os.getcwd()
os.chdir("../OAGen")
oagen_path = os.getcwd()
os.chdir("../DroidScraper")

for memdump_foldername in os.listdir(memdumps_path):
    try:
        print "Starting HeapDump with " + memdump_foldername
        heapdump_filename = memdump_foldername + "_heapdump.out"
        command = "python " + droidscraper_path + "/artProj.py " + memdumps_path + "/" + memdump_foldername + " HeapDump > " + heapdumps_path + "/" + heapdump_filename
        #print (command)
        return_code = os.system(command)
        if return_code == 0:
            print "HeapDump " + memdump_foldername + " completed successfully"
        else:
            print "HeapDump " + memdump_foldername + " failed with exit code " + return_code
    except Exception as e:
        print "Exception in " + memdump_foldername + ": " + str(e)