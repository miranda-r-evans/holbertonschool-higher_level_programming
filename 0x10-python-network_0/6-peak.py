#!/usr/bin/python3
'''
algorithm to find a peak (local maximum) in a data set
'''


def find_peak(list_of_integers):
    '''
    algorithm to find a peak (local maximum) in a data set
    '''

    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) // 2

    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

    is_end = len(list_of_integers) == 2
    condition1 = list_of_integers[mid] > list_of_integers[mid - 1]
    condition2 = (is_end or list_of_integers[mid] > list_of_integers[mid + 1])

    if condition1 and condition2:
        return list_of_integers[mid]

    if is_end and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])

    try:
        right = find_peak(list_of_integers[mid + 1:])
    except:
        right = None

    left = find_peak(list_of_integers[:mid])

    if right is None or right < left:
        return left

    return right
