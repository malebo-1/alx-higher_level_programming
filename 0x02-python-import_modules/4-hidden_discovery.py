#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # sorted name to be printed from the directory
    for name in sorted(dir(hidden_4)):
        # only names that do not start with __ must be printed
        if name[:2] != '__':
            print("{}".format(name))
