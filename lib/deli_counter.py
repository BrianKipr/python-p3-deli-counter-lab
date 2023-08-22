# lib/deli_counter.py

def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for i, person in enumerate(deli_line, start=1):
            line_str += f" {i}. {person}"
        print(line_str)

def take_a_number(deli_line, name):
    deli_line.append(name)
    position = len(deli_line)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving = deli_line.pop(0)
        print(f"Currently serving {serving}.")

# Test cases
KATZ_DELI = []
OTHER_DELI = ["Logan", "Avi", "Spencer"]
ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]
