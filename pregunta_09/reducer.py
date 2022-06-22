#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


if __name__ == '__main__':

    orden= [] 
    for line in sys.stdin:

        key, val1, val2 = line.strip().split(",")
        val2 = int(val2)
        orden.append([key,val1,val2])
    

    elements = sorted(orden, key =lambda x:(x[2]))
    
    for i in range(0,6):
        sys.stdout.write("{}   {}   {}\n".format(elements[i][0],elements[i][1],elements[i][2]))