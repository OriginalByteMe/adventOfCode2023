with open('day_1/input.txt', 'r') as f:  # Open file for read
    total = 0
    for line in f:           # Read line-by-line
        line_chars = []
        line = line.strip()
        for char in line: 
          if char.isdigit():
            line_chars.append(char)
        
        num_str = line_chars[0] + line_chars[-1]
        total += int(num_str)

    print(total)
