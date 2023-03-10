import sys
import argparse
import random

sys.tracebacklimit = 0

def generator(text : str, option=None, sep=' '):
    try:
        str(text)
        splitted = text.split(sep)
        if option == 'ordered':
            splitted.sort()
        elif option == 'shuffle':
            random.shuffle(splitted)
        elif option == 'unique':
            splitted = set(splitted)
        for i in splitted:
            yield i
    except:
        print("ERROR")
        return ;


def main(args : list) -> None:
    for word in generator(args[0], sep=' '):
        print(word)

def validate_arg(args : list):
    assert len(args) == 1 and str(args[0]), "Usage : python3 generator.py \"String\""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    validate_arg(args)
    return args

if __name__ == "__main__":
    main(get_args())