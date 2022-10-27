def f_break():
    lb = "-" * 50
    print(lb)


for i in range(1, 6):
    print(i)
    if i == 3:
        break


f_break()


for i in range(1, 6):
    print(i)
else:
    print("i is not longer in the range")


f_break()

