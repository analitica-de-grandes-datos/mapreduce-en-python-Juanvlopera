#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    lista=[]
    for line in sys.stdin:
        key, val1 = line.strip().split("\t")
        val2 = val1.strip().split(",")
        #orden.append(val2)
        for letra in val2:
            sys.stdout.write("{}\t{}\n".format(letra,key))