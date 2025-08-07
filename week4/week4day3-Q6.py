from typing import List

def splitList(List):
    mid = len(List) // 2
    first = List[:mid]
    last = List[mid:]
    print(first)
    print(last)

list = ["Anirudh", 6, 4, 110.654, True, -54]
splitList(list)