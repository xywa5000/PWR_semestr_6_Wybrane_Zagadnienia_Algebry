import sys
from itertools import product
from typing import List
from random import shuffle
import matplotlib.pyplot as plt


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

def plot_points(all_points: List[List[int]], minimal_points: List[List[int]], title: str) -> None:
    all_x, all_y = zip(*all_points)
    min_x, min_y = zip(*minimal_points)
    
    plt.figure(figsize=(10, 10))
    plt.scatter(all_x, all_y, label='All Points', color='blue')
    plt.scatter(min_x, min_y, label='Minimal Points', color='red')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.xticks(range(0, 21))
    plt.yticks(range(0, 21))
    plt.grid(True, which='major', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.legend()
    plt.show()

def main() -> int:
    s1 = DataSet(2, func1, border1)
    points1 = s1.gen_points(0, 20)
    minimal1 = find_minimal(points1)
    print("Minimal points for DataSet 1:", minimal1)
    
    s2 = DataSet(2, func2, border2)
    points2 = s2.gen_points(0, 20)
    minimal2 = find_minimal(points2)
    print("Minimal points for DataSet 2:", minimal2)
    
    # Plotting the points
    plot_points(points1, minimal1, 'DataSet 1')
    plot_points(points2, minimal2, 'DataSet 2')
    return 0

if __name__ == '__main__':
    sys.exit(main())
