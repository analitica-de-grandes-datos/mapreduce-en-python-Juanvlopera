#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    suma = None
    promedio = None
    count=0
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            suma += val
            count+= 1
            promedio = suma/count
        else:
            if curkey is not None:
                promedio=suma/count
                sys.stdout.write("{}\t{}\t{}\n".format(curkey,suma,promedio))
                
            curkey = key
            suma = val
            count=1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey,suma,promedio))