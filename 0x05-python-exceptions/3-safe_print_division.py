#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        result = None
    except Exception as e:
        print("An error occurred:", e)
        result = None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
        return result
