# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 10:44:42 2016

@author: Dave Ho
"""

class Item():
    def __init__(self, name, value, weight):
        self.name = name
        self.value = float(value)
        self.weight = float(weight)
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
                + ', ' + str(self.weight) + '>'
        return result

def build_items():
    names = ['frisbee', 'ball', 'headphone', 'book', 'poker']
    values = [5, 20, 25, 45, 2]
    weights = [0.4, 2.2, 1.2, 2, 0.6]
    items = []
    for i in range(0, len(names)):
        items.append(Item(names[i], values[i], weights[i]))
    return items

def greedy_value(items, capacity):
    copy_items = sorted(items, key=lambda item: item.value, reverse=True)
    sack = []
    current_capacity = capacity
    for item in copy_items:
        if item.weight < current_capacity:
            sack.append(str(item))
            current_capacity -= item.weight
        elif current_capacity == 0:
            break
    return sack

def greedy_weight(items, capacity):
    copy_items = sorted(items, key=lambda item: item.weight)
    sack = []
    current_capacity = capacity
    for item in copy_items:
        if item.weight < current_capacity:
            sack.append(str(item))
            current_capacity -= item.weight
        elif current_capacity == 0:
            break
    return sack

def greedy_ratio(items, capacity):
    copy_items = sorted(items, key=lambda item: item.value/item.weight, reverse=True)
    sack = []
    current_capacity = capacity
    for item in copy_items:
        if item.weight < current_capacity:
            sack.append(str(item))
            current_capacity -= item.weight
        elif current_capacity == 0:
            break
    return sack

def generate_powerset(items):
    numsub = 2**len(items)
    binary = []
    for i in range(0, numsub):
        binary.append(bin(i)[2:].zfill(len(items)))
    powerset = []
    for b in binary:
        element = []
        for i in range(0, len(b)):
            if b[i] == '1':
                element.append(str(items[i]))
        powerset.append(element)
    return powerset

def genpset(items):
    result = []
    if len(items) == 0:
        return [[]]
    rest = genpset(items[1:])
    for i in rest:
        result.append(i)
        result.append(i + [items[0]])
    return result

def brute_force(items, capacity):
    pset = genpset(items)
    maxval = -1
    maxsub = None
    totval = 0
    totweight = 0
    for sub in pset:
        for item in sub:
            totweight += item.weight
            totval += item.value
        if totweight < capacity:
            if totval > maxval:
                maxval = totval
                maxsub = sub
        totval = 0
        totweight = 0
    return [str(i) for i in maxsub]