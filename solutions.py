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
    def palindromic_phrases(cls, phrase: str) -> int:

        stripped_phrase = phrase.replace(" ", "").lower()
        revered_phrase = stripped_phrase[::-1]
        return int(stripped_phrase == revered_phrase)

    @classmethod
    def count_factors_2(cls, pint: int) -> int:

        factors: int = 0
        for num in range(1, pint + 1):
            if pint % num == 0:
                factors += 1
        return factors

    @classmethod
    def zany_zebras(cls, zebra_heights: List[int]) -> int:

        height_sum = sum(zebra_heights)
        average = round(height_sum/len(zebra_heights))
        return floor(average)

    @classmethod
    def evans_elephants(cls, distance: int, start_energy: List[int], lose_energies: List[int]) -> int:

        energy_lost: List[int] = [energy * distance for energy in lose_energies]
        died: int = 0
        for i in range(len(lose_energies)):

            if start_energy[i] < energy_lost[i]:
                died += 1
        return died
