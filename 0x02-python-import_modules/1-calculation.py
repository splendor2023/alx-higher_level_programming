
#!/usr/bin/python3

import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5

    result_add = calculator_1.add(a, b)
    print("The sum of {} and {} is: {}".format(a, b, result_add))

    result_subtract = calculator_1.subtract(a, b)
    print("The difference between {} and {} is: {}".format(a, b, result_subtract))

    result_multiply = calculator_1.multiply(a, b)
    print("The product of {} and {} is: {}".format(a, b, result_multiply))

    result_divide = calculator_1.divide(a, b)
    print("The division of {} by {} is: {}".format(a, b, result_divide))
