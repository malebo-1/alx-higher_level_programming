#!/usr/bin/python3
def add_arg(argv):
    j = len(argv) - 1
    if j == 0:
        print("{:d}".format(j))
        return
    else:
        k = 1
        add = 0
        while k <= j:
            add += int(argv[k])
            k += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
