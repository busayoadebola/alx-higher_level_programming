#!/usr/bin/python3
import sys

def mes_body():
    message = "and that piece of art is useful - Dora Korpar, 2015-10-19"
    sys.stderr.write(message + '\n')
    sys.exit(1)

if __name__ == "__main__":
    mes_body()
