#!/usr/bin/env python3

def can_be_a_set_member_or_frozenset(item):
    '''
    Find out whether the input item can be part of a set,
    if yes, return it as is, otherwise return it as a frozenset
    '''

    # create an empty set and try to add the input item to it
    x = set()
    try:
        x.add(item)
    except:
        # if adding the item failed, return it as a frozenset
        return frozenset(item)
    
    return item 

def all_subsets(lst):
    '''
    Create a list of all of the input set's subsets as lists.
    Input set is given to the function as a list.
    '''

    # create list of subsets and add empty set to it
    sublist = [[]]
    # create subsets from original set and append them to subset list
    for item in lst:
        copy=sublist.copy()
        for x in copy:
            tmp = x.copy()
            tmp.append(item)
            sublist.append(tmp)
    
    return sublist

def all_subsets_excl_empty(*args, exclude_empty = True):
    '''
    Create a list of all the input arguments and then a list of all
    subsets as lists.
    If the input argument 'exclude_empty' is set to True or not set,
    return the list without the empty list.
    '''

    # create a list of all the input arguments
    lst = []
    for item in args:
        lst.append(item)

    # create a list of all the arguments' subsets.        
    sublist = [[]]
    for item in lst:
        copy=sublist.copy()
        for x in copy:
            tmp = x.copy()
            tmp.append(item)
            sublist.append(tmp)    

    # remove empty list if asked to do so or if the option is not set
    if exclude_empty:
        sublist.remove(list([]))

    return sublist
