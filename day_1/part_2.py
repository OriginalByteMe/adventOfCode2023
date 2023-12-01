import re

number_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


with open("day_1/input.txt") as f:
    input = [line.strip() for line in f.readlines()]

total = 0    
for line in input:
  num_string = ""
  numbers = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9])){1}", line)
  
  # Convert words to numbers using the number_words dictionary
  numbers = [number_words.get(item, item) for item in numbers]
  
  total += (int(numbers[0] + numbers[-1]))

print("TOTAL:", total)
      




  
