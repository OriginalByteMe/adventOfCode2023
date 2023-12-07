import re
import math

with open("day_4/input.txt") as f:
    cards = [line.strip() for line in f.readlines()]

task_1 = 0
task_2 = 0

for card in cards:
    card = re.sub(r"Card\s+\d+:", "", card)
    numbers = card.split("|")
    winning_numbers = [num for num in re.split(r"\s+", numbers[0]) if num]
    recieved_numbers = [num for num in re.split(r"\s+", numbers[1]) if num]
    intersect_count = len(set(winning_numbers) & set(recieved_numbers))

    task_1 += 2 ** (intersect_count - 1) if intersect_count > 0 else 0


print("Task 1: ", task_1)
