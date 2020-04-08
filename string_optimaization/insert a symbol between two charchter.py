
import re

with open('test.txt', 'r') as input, open('out.txt', 'w') as output:
    output.write("[\n")
    for line in input:
        line = re.sub('}{', '},{', line)
        output.write('    '+line)
    output.write("]\n")
