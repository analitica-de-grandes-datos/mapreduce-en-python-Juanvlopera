#
# >>> Escriba el codigo del reducer a partir de este punto <<<
import sys

if __name__ == '__main__':

    orden= {} 
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        orden[key] = val
    def take_value(key):
        return key[1]
    elements = sorted(orden.items(), key = take_value)
    
    for element in elements:
        sys.stdout.write("{},{}\n".format(element[0], element[1]))
