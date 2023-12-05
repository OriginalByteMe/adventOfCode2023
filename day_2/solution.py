import re

R_MAX = 12
G_MAX = 13
B_MAX = 14
task_1 = 0
task_2 = 0

with open("day_2/input.txt") as f:
    games = [line.strip() for line in f.readlines()]

for game in games:
    highest_red_count = 0
    highest_green_count = 0
    highest_blue_count = 0

    lowest_red_count = float("inf")
    lowest_green_count = float("inf")
    lowest_blue_count = float("inf")

    game_id, rounds = game.split(": ")
    rounds = rounds.split("; ")
    print(f"Task 2, previous game: {task_2}")
    for round in rounds:
        colors = round.split(", ")

        for color in colors:
            count, color = color.split(" ")
            count = int(count)
            if color == "red":
                highest_red_count = max(highest_red_count, count)
            elif color == "green":
                highest_green_count = max(highest_green_count, count)
            elif color == "blue":
                highest_blue_count = max(highest_blue_count, count)


    task_2 += highest_blue_count * highest_green_count * highest_red_count

    if (
        highest_blue_count > B_MAX
        or highest_green_count > G_MAX
        or highest_red_count > R_MAX
    ):
        continue

    task_1 += int(game_id.split(" ")[1])

print("Task 1: ", task_1)
print("Task 2: ", task_2)
