#!/bin/python3

# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    pass
    


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')