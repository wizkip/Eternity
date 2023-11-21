
from itertools import permutations


def simple(str):

    permlist = permutations(str)

    for perm in list(permlist):

        print(''.join(perm))

if __name__ == "__main__":

    str = "AWS"

    simple(str)

    