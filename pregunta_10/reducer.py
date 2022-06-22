#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    orden= [] 
    for line in sys.stdin:

        key, val1 = line.strip().split("\t")
        val1=int(val1)
        orden.append([key,val1])
    

    elements = sorted(orden, key =lambda x:(x[0],x[1]))
    
    curkey = None
    total = str(0)
    for element in elements:
        key=element[0]
        val=str(element[1])
        if element[0] == curkey:
            total =total+","+val
        else:
            if curkey is not None:
               sys.stdout.write("{}\t{}\n".format(curkey, total))
            curkey = key
            total = val
    sys.stdout.write("{}\t{}\n".format(curkey, total))