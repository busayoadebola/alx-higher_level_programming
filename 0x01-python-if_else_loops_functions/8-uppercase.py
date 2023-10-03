#!/usr/bin/python3
def uppercase(str):
    converted = ""
    for char in str:
        if "a" <= char <= "z":
            """ Convert from lower case to uppercase """
            converted += chr(ord(char) - ord("a") + ord("A"))
        else:
            converted += char
    print("{}".format(converted))
