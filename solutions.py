from typing import List
from math import floor, sqrt


class Solutions:

    @classmethod
    def number_strings(cls, string: str) -> int:

        abc = "abcdefghijklmnopqrstuvwxyz"
        tally = 0
        for char in string:
            index = abc.index(char) + 1
            tally += index
        return tally

    @classmethod
    def triangle_side_solver(cls, side1: int, side2: int) -> int:

        a = pow(side1, 2)
        b = pow(side2, 2)
        ab = a + b
        hypotenuse = sqrt(ab)
        return round(hypotenuse)

    @classmethod
    def zany_zebras(cls, zebra_heights: List[int]) -> int:

        height_sum = sum(zebra_heights)
        average = round(height_sum/len(zebra_heights))
        return floor(average)




