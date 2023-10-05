#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    add_no = add(a, b)
    sub_no = sub(a, b)
    mul_no = mul(a, b)
    div_no = div(a, b)
    print("{} + {} = {}".format(a, b, add_no))
    print("{} - {} = {}".format(a, b, sub_no))
    print("{} * {} = {}".format(a, b, mul_no))
    print("{} / {} = {}".format(a, b, div_no))
