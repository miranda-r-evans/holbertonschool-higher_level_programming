#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new = []
    for index in range(list_length):
        try:
            new.append(my_list_1[index] / my_list_2[index])
        except TypeError:
            print('wrong type')
            new.append(0)
        except ZeroDivisionError:
            print('division by 0')
            new.append(0)
        except IndexError:
            print('out of range')
            new.append(0)
    return new
