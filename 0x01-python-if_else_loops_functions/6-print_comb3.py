#!/usr/bin/python3
for first_no in range(10):
    for second_no in range(first_no + 1, 10):
        print("{:02d}, ".format(first_no * 10 + second_no), end="")
print("\n")

