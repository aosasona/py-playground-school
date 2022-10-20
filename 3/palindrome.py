def reverse_number(num: int) -> int:
    string_num = str(num)
    length = len(string_num)
    if length < 2:
        print("Number is too short")
        exit(1)
    reversed_str = string_num[::-1]
    return int(reversed_str)


x = int(input("Enter a number greater than 9: "))


def compare(num: int):
    num_mirror = reverse_number(num)
    if x == num_mirror:
        return True


if compare(x):
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")
