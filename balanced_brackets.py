#!/bin/python3

from collections import deque

OPEN_COLCHETES = '['
CLOSE_COLCHETES = ']'
OPEN_PARENTESIS = '('
CLOSE_PARENTESIS = ')'
OPEN_CHAVES = '{'
CLOSE_CHAVES = '}'

CLOSERS = [CLOSE_COLCHETES, CLOSE_PARENTESIS, CLOSE_CHAVES]
CHAVES = [OPEN_CHAVES, CLOSE_CHAVES]
PARENTESIS = [OPEN_PARENTESIS, CLOSE_PARENTESIS]
COLCHETES = [OPEN_COLCHETES, CLOSE_COLCHETES]


def isChave(character):
    return character in CHAVES


def isParentesis(character):
    return character in PARENTESIS


def isColchete(character):
    return character in COLCHETES


def isCloser(character):
    return character in CLOSERS


# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    pilha = deque()

    for element in enumerate(brackets):
        if isCloser(element):
            if not len(pilha):
                return 'NO'  # Caracter de fechar com pilha vazia

            if isChave(element):
                if not isChave(pilha[-1]):
                    return 'NO'  # Fechando chaves fora de ordem
                pilha.pop()  # Match de chaves!

            elif isParentesis(element):
                if not isParentesis(pilha[-1]):
                    return 'NO'  # Fechando parentesis fora de ordem
                pilha.pop()  # Match de parentesis!

            elif isColchete(element):
                if not isColchete(pilha[-1]):
                    return 'NO'  # fechando colchete fora de ordem
                pilha.pop()  # Match de colchete!

        else:
            pilha.append(element)  # Caracter de abrir

    if not len(pilha):
        return 'YES'  # Todos os caracteres deram match
    return 'NO'  # Ha caracteres que nao deram match


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
