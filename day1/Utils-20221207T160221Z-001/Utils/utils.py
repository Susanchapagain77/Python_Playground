ERROR_COLOR = "\033[1;31m"
SUCCESS_COLOR = "\033[1;32m"
WARN_COLOR = "\033[1;33m"
INFO_COLOR = "\033[1;34m"
END_COLOR = "\033[0;0m"


# test case for function simple_interest
def test_simple_interest(fn):
    """
    Error handling not done on purpose to show the students the possibility of syntactical and logical error
    Possible Exceptions: ZeroDivisionError or SyntaxError

    """
    test_data = {(100, 2, 2): 4,
                 (100, 3, 10): 30,
                 (1000, 5, 15): 750,
                 (45000, 5, 10): 22500,
                 (12315100, 3, 10): 3694530
                 }
    i = 0
    score = 0
    for (p, t, r), si in test_data.items():
        returned_si = fn(p, t, r)
        if si == returned_si:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# test case for function smallest_number
def test_smallest_number(fn):
    test_data = {(1, 2, 0): 0,
                 (3, 2, 19): 2,
                 (20, 20, 5): 5,
                 (5, 5, 10): 5,
                 (11, 11, 11): 11,
                 (-1, 3, 10): -1
                 }
    i = 0
    score = 0
    for (n1, n2, n3), smallest in test_data.items():
        returned_smallest = fn(n1, n2, n3)
        if smallest == returned_smallest:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# test case for function math_operation
def test_math_operation(fn):
    test_data = {(10, 2, "+"): 12,
                 (9, 7, "-"): 2,
                 (1, 7, "-"): -6,
                 (9, 7, "*"): 63,
                 (0, 7, "*"): 0,
                 (21, 7, "/"): 3,
                 (21, 0, "/"): "Divide by zero",
                 (21, 2, "%"): "invalid operator",
                 }
    i = 0
    score = 0
    for (n1, n2, op), result in test_data.items():
        returned_result = fn(n1, n2, op)
        if result == returned_result:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# test case for function factorial
def test_factorial(fn):
    test_data = {6: 720,
                 10: 3628800,
                 26: "number too large",
                 21: 51090942171709440000,
                 25: 15511210043330985984000000,
                 0: 1,
                 1: 1,
                 }
    i = 0
    score = 0
    for num, fact in test_data.items():
        returned_fact = fn(num)
        if fact == returned_fact:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# test case for function factorial
def test_fibonacci(fn):
    test_data = {0: 0,
                 1: 1,
                 3: 2,
                 4: 3,
                 9: 34,
                 10: 55,
                 12: 144,
                 13: 233,
                 15: 610,
                 19: 4181,
                 }
    i = 0
    score = 0
    for num, fibo in test_data.items():
        returned_fibo = fn(num)
        if fibo == returned_fibo:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# function for calculating final score
def final_score(score):
    total_score = len(score)
    obtained_score = sum(list(score.values()))
    print(f"Total Score: \033[1;34m{total_score}\033[0;0m")
    if obtained_score:
        print(f"Obtained Socre: {SUCCESS_COLOR} {obtained_score} {END_COLOR}")
    else:
        print(f"Obtained Socre: {ERROR_COLOR} {obtained_score} {END_COLOR}")
