from utils import split_nums

raw_numbers = input(">> Enter numbers separated by commas or space: ")

num_list = split_nums(raw_numbers)

count = {
    "even": 0,
    "odd": 0,
    "zero": 0
}

for num in num_list:
    if num != 0:
        if num % 2 == 0:
            count["even"] += 1
        else:
            count["odd"] += 1
    else:
        count["zero"]

print(f"There were {count['even']} even numbers, {count['odd']} odd numbers and {count['zero']} zero numbers.")