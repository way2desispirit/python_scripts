#!/usr/bin/env python3
import random
n = random.randint(1, 10)
print("Converting {} random decimal numbers between 1-1000 to its equivalent binary.\n "
      "The decimal numbers are stored in intermediate_output.txt and its corresponding binary values are in final_output.txt".format(n))
with open("intermediate_output.txt","w") as fp:
    fp.write(str(random.sample(range(1, 1000), n)).strip("[").strip("]"))
with open("intermediate_output.txt","r") as fp:
    for line in fp:
        dec = line.split(",")
with open("intermediate_output.txt","r") as fp:
    a = fp.read()
with open("final_output.txt","w") as fp:
    fp.write(str(list(map(lambda x: int(bin(int(x))[2:]), a.split(",")))).strip("[").strip("]"))
