#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random as rnd
from collections import deque


def create(length, max_value):
    unique_numbers = list(range(max_value))
    rnd.shuffle(unique_numbers)
    return unique_numbers[:length]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        middle = len(arr) // 2
        left, inv_left = merge_sort(arr[:middle])
        right, inv_right = merge_sort(arr[middle:])
        merged, inv_merge = merge(deque(left), deque(right))
        return merged, inv_left + inv_right + inv_merge


def merge(left, right):
    merged = []
    inv_count = 0
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.popleft())
        else:
            merged.append(right.popleft())
            inv_count += len(left)
    merged.extend(left)
    merged.extend(right)
    return merged, inv_count


if __name__ == '__main__':
    array = create(5, 100)
    print("Array =", array)
    _, count = merge_sort(array)
    print("Количество инверсий в массиве =", count)