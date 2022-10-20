from utils import split_nums

raw_numbers = input(">> Enter three numbers separated by a comma or space: ")
maximum = max(split_nums(raw_numbers))
print("The maximum is:", maximum)



