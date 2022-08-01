"""
ID: eshaant1
LANG: PYTHON3
TASK: ride
"""

from tokenize import group


fin = open("ride.in","r")
fout = open("ride.out","w")

comet=fin.readline()
groups=fin.readline()

cometProd=1
groupsProd=1

for letter in comet:
    cometProd=cometProd*(ord(letter)-64)

for alph in groups:
    groupsProd=groupsProd*(ord(alph)-64)

if ((cometProd % 47) == (groupsProd % 47)):
    fout.write("GO\n")

else:
    fout.write("STAY\n")
    fout.close()
    fin.close()

