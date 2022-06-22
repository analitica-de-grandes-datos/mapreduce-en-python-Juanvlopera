#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        limpiar = line.strip()
        sys.stdout.write("{}\t{}\n".format(limpiar.split("  ")[0],limpiar.split("  ")[2]))