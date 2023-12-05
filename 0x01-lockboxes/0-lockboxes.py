#!/usr/bin/python3
'''This file contains a function that determines if all of the boxes can be opened'''


def canUnlockAll(boxes):
    '''Lockboxes'''
    keys = [*boxes[0]]
    i = 0
    while (i < len(keys)):
        for j in range(len(boxes[keys[i]])):
            if boxes[keys[i]][j] not in keys and boxes[keys[i]][j] != 0:
                keys.append(boxes[keys[i]][j])
        i += 1

    return len(keys) == len(boxes) - 1
