#!/usr/bin/python3
''' module that contains a list subclass '''


class MyList(list):
    ''' prints a sorted version of the list '''
    def print_sorted(self):
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
        del sorted_list
