import re

with open("day_3/input.txt") as f:
    schematic = [line.strip() for line in f.readlines()]

task_1 = 0
task_2 = 0

symbols = set(["*", "$", "#", "+", "%", "-", "@", "/", "&", "="])

unique_chars = set()

for line in schematic:
    for char in line:
        if not char.isdigit() and char != ".":
            unique_chars.add(char)

print(unique_chars)

for i, line in enumerate(schematic):
    # Find all numbers in the line
    for match in re.finditer(r"\d+", line):
        start_index = match.start()
        end_index = match.end() - 1
        number = match.group()
        adjacent_chars = []
        # Check the same line
        if start_index > 0:
            adjacent_chars.append(line[start_index - 1])
        if end_index < len(line) - 1:
            adjacent_chars.append(line[end_index + 1])
        # Check the previous line
        if i > 0:
            # Append all top adjacent chars
            for char in schematic[i - 1][start_index : end_index + 1]:
                adjacent_chars.append(char)

            # Append the top left and top right adjacent chars
            if start_index > 0:
                adjacent_chars.append(schematic[i - 1][start_index - 1])
            if end_index < len(line) - 1:
                adjacent_chars.append(schematic[i - 1][end_index + 1])
        # Check the next line
        if i < len(schematic) - 1:
            # Append all bottom adjacent chars
            for char in schematic[i + 1][start_index : end_index + 1]:
                adjacent_chars.append(char)

            # Append the bottom left and bottom right adjacent chars
            if start_index > 0:
                adjacent_chars.append(schematic[i + 1][start_index - 1])
            if end_index < len(line) - 1:
                adjacent_chars.append(schematic[i + 1][end_index + 1])
        # If any adjacent character is a symbol, add the number to task_1
        if any(adj_char in unique_chars for adj_char in adjacent_chars):
            task_1 += int(number)

print("Task 1: ", task_1)

for i, line in enumerate(schematic):
    for j, char in enumerate(line):
        if char == '*':
            adjacent_numbers = []
            # Check the same line
            if j > 0 and re.match(r'\d+', line[j-1]):
                adjacent_numbers.append(int(re.match(r'\d+', line[j-1:]).group()))
            if j < len(line) - 1 and re.match(r'\d+', line[j+1]):
                adjacent_numbers.append(int(re.match(r'\d+', line[j+1:]).group()))
            # Check the previous line
            if i > 0:
                if re.match(r'\d+', schematic[i-1][j:]):
                    adjacent_numbers.append(int(re.match(r'\d+', schematic[i-1][j:]).group()))
            # Check the next line
            if i < len(schematic) - 1:
                if re.match(r'\d+', schematic[i+1][j:]):
                    adjacent_numbers.append(int(re.match(r'\d+', schematic[i+1][j:]).group()))
            # If there are at least two numbers adjacent to the symbol, multiply them and add to task_2
            if len(adjacent_numbers) == 2:
                print("Found two adjacent numbers: ", adjacent_numbers)
                task_2 += adjacent_numbers[0] * adjacent_numbers[1]

print("Task 2: ", task_2)
    
