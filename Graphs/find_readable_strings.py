import sys

#txtfile = sys.argv[1]

txtfile = '/home/kutti/KLTN/Graphs/testing/Whatsapp_memdump_29052023_heapdump_graph_strings.txt'

txt_words = txtfile.split('.')[0] + "_readable.txt"

lines_with_words = []

with open(txtfile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split()
        if len(words) > 4:
            lines_with_words.append(line)

with open(txt_words, 'w') as f:
    f.writelines(lines_with_words)