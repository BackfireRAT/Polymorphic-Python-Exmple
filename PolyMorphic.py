import os
import subprocess
from random import randint
# 1
def Morph():
    String = "a"
    file = open(__file__,'r')
    Original = file.read()
    Lines = Original.split("\n")
    for _ in range(len(Lines)):
        Split = Lines[_].split(" ")
        for __ in range(len(Split)):
            if (Split[0] == "def"):
                num = randint(1,9)
                for a in range(num):
                    String = String + str(randint(1,99999))
                FName = String
                Split[1] = String + "():"
            else:
                if (Split[0] == "#"):
                    Split[1] = str(int(Split[1]) + 1)
                    Version = Split[1]
                else:
                    try:
                        if (Split[1] == "##"):
                            Split[0] = FName + "()"
                    except:
                        pass
        Lines[_] = " ".join(Split)
    New = "\n".join(Lines)
    try:
        file2 = open(FName + ".py",'w')
        file2.write(New)
    except:
	file2 = open("1inamillion.py",'w')
        file2.write(New)
    file.close()
    file2.close()
Morph() ##
