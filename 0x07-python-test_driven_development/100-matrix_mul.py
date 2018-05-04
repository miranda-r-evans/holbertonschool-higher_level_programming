#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    if isinstance(m_a, list) is False:
        raise TypeError('m_a must be a list')
    if isinstance(m_b, list) is False:
        raise TypeError('m_b must be a list')
    if m_a == []:
        raise ValueError('m_a can\'t be empty')
    if m_b == []:
        raise ValueError('m_b can\'t be empty')

    if isinstance(m_a[0], list) == True:
        if len(m_a[0]) != 0:
            a_row = len(m_a[0])
        else:
            raise ValueError('m_a can\'t be empty')
    else:
        raise TypeError('m_a must be a list')

    if isinstance(m_b[0], list) == True:
        if len(m_b[0]) != 0:
            b_row = len(m_b[0])
        else:
            raise ValueError('m_b can\'t be empty')
    else:
        raise TypeError('m_b must be a list')

    for row in m_a:
        if isinstance(row, list) is False:
            raise TypeError('m_a must be a list')
        if len(row) != a_row:
            raise TypeError('each row of m_a must should be of the same size')
        if all(isinstance(num, (int, float)) for num in row) is False:
            raise TypeError('m_a should contain only integers or floats')

    for row in m_a:
        if isinstance(row, list) is False:
            raise TypeError('m_b must be a list')
        if len(row) != b_row:
            raise TypeError('each row of m_b must should be of the same size')
        if all(isinstance(num, (int, float)) for num in row) is False:
            raise TypeError('m_b should contain only integers or floats')

    if a_row != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    new = []
    row_count = 0
    for a_row in m_a:
        row_count = 0
        row_to_add = []
        for row_count in range(b_row):
            num_to_add = 0
            col_count = 0
            for a_col in a_row:
                num_to_add = num_to_add + a_col * m_b[col_count][row_count]
                col_count = col_count + 1
            row_to_add.append(num_to_add)
        new.append(row_to_add)

    return new
