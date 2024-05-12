import sys
from itertools import product
from typing import List
from random import shuffle

class DataSet():
    def __init__(self, expo: int, value_func, border_func) -> None:
        self.expo = expo
        self.border_func = border_func
        self.value_func = value_func
        
    def gen_points(self, low_border: int, high_border: int) -> List:
        ranges_list = [range(low_border, high_border) for _ in range(self.expo)]
        all_points = product(*ranges_list)
        set_points = (point for point in all_points if self.border_func(self.value_func(point)))
        set_points = list(set_points)  # Convert generator to list
        shuffle(set_points)
        # print(set_points)
        return set_points

def evaluate(point1: List[int], point2: List[int]) -> bool:
    for x, y in zip(point1, point2):
        if x > y:
            return False
    return True

def find_minimal(points: List[List[int]]) -> List[List[int]]:
    minimal = set()
    for a in points:
        to_add = True
        to_remove = set()
        for m in minimal:
            if evaluate(m, a):
                to_add = False
                break
            if evaluate(a, m):
                to_remove.add(m)
        if to_add:
            minimal.add(tuple(a))
            minimal -= to_remove
    return [list(point) for point in minimal]

def func1(point: List[int]) -> int:
    return point[0] * point[1]

def func2(point: List[int]) -> int:
    return (point[0] - 10) ** 2 + (point[1] - 10) ** 2

def border1(value: int) -> bool:
    return value >= 11

def border2(value: int) -> bool:
    return value <= 25

def main() -> int:
    s1 = DataSet(2, func1, border1)
    points = s1.gen_points(0, 10)
    minimal = find_minimal(points)
    print(minimal)
    s2 = DataSet(2, func2, border2)
    points = s2.gen_points(0, 10)
    minimal = find_minimal(points)
    print(minimal)
    return 0

if __name__ == '__main__':
    sys.exit(main())
