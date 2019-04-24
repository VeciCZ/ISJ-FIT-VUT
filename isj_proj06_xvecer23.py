#!/usr/bin/env python3
import itertools


def first_nonrepeating(string):
    ''' Find the first letter in a string that occurs only once in it. '''

    badtypes = [list, tuple, int, dict, set]
    if type(string) in badtypes or len(string) == 0:
        return None
    
    letters = {}
    for i in string:
        if i.isspace():
            continue
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    if letters == {}:
        return None

    for i in letters:
        if letters[i] == 1:
            return i

    return None


def combine4(numbers, result):
    '''
        Receive four numbers and an expected result and return all
        solutions containing those numbers which lead to the result.
    '''

    if len(numbers) != 4:
        return None
    
    numcomb = sorted(list(set(itertools.permutations(numbers))))
    operations = list(itertools.product(['+', '-', '*', '/'], repeat=3))
    brackets = [['(', '', ')', '', ''], ['(', '', ')(', '', ')'],
                ['', '', '(', '', ')'], ['', '(', '', ')', ''],
                ['(', '', '', ')', ''], ['((', '', ')', ')', ''],
                ['(', '(', '', '))', ''], ['', '(', '', '', ')'],
                ['', '((', '', ')', ')'], ['', '(', '(', '', '))']]
    bracketsclose = [')', '))']
    bracketsopen = ['(', '((']

    solutions = []
    for i in range(len(brackets)-1):
        for j in range(len(operations)-1):
            for k in range(len(numcomb)):
                solution = str(brackets[i][0]) + str(numcomb[k][0])
                for l in range(1,4):
                    if brackets[i][l] == '':
                        solution += str(operations[j][l-1])
                    elif brackets[i][l] in bracketsclose:
                        solution += str(brackets[i][l]) + str(operations[j][l-1])
                    elif brackets[i][l] in bracketsopen:
                        solution += str(operations[j][l-1]) + str(brackets[i][l])
                    elif brackets[i][l] == ')(':
                        solution += ')' + str(operations[i][l-1]) + '('
                    if l < 4:
                        solution += str(numcomb[k][l])
                solution += brackets[i][4]

                try:
                    if eval(solution) == result:
                        solutions.append(solution)
                except ZeroDivisionError:
                    continue

    return sorted(list(set(solutions)))
