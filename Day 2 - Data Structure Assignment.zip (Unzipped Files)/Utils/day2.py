ERROR_COLOR = "\033[1;31m"
SUCCESS_COLOR = "\033[1;32m"
WARN_COLOR = "\033[1;33m"
INFO_COLOR = "\033[1;34m"
END_COLOR = "\033[0;0m"


# test case for function comma_code
def test_comma_code(fn):
    """
    Error handling not done on purpose to show the students the possibility of syntactical and logical error
    Possible Exceptions: ZeroDivisionError or SyntaxError

    """
    test_data = {('apples','bananas','car','dog'): 'apples,bananas,car,dog',
                 (1,5,True,3,'day'): '1,5,True,3,day',
                 (2,'dogs',5,'cats','mouse'): '2,dogs,5,cats,mouse'
                 }
    i = 0
    score = 0
    for mylist, si in test_data.items():
        returned_si = fn(list(mylist))
        if si == returned_si:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# test case for function list_operations
def test_list_operations(fn):
    test_data = {((5,2,7),12,1,10): [10,7,5,2],
                 ((),5,0,3): [3],
                 ((3,1,5,15,2),8,3,9): [9,8,5,3,2,1],
                 ((19,),8,0,9): [9,8],
                 ((5,2),16,2,9): [9,5,2]
                 }
    i = 0
    score = 0
    for (mylist, a, i, e), output in test_data.items():
        returned_output = fn(list(mylist), a, i, e)
        if output == returned_output:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# test case for function lowest_score
def test_lowest_score(fn):
    test_data = {(('Harry', 37.21), ('Berry', 37.21), ('Tina', 37.2), ('Akriti', 41), ('Harsh', 39)): "Tina",
                 (("chi",20.0),("beta",52.1),("gamma",15)): "gamma",
                 (("ram",80.0),("sita",78),("gopal",92),("hari",45.32)): "hari"
                 }
    i = 0
    score = 0
    for students, result in test_data.items():
        returned_result = fn(list(students))
        if result == returned_result:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# test case for function average_score
def test_average_score(fn):
    test_data = [({"alpha":[20,30,40],"beta":[30,50,70]}, {"alpha":30,"beta":50}),
                 ({"ram":[40,90,200],"hari":[30,50,70],"gita":[88,52,50,70]}, {'ram': 110.0, 'hari': 50.0, 'gita': 65.0}),
                 ({"jack":[45,90,50,92,53,85,75]}, {"jack":70.0})
                ]
    i = 0
    score = 0
    for student, average in test_data:
        returned_average = fn(student)
        if average == returned_average:
            print(f" Test {i}:{SUCCESS_COLOR} Passed {END_COLOR}")
            score += 1
        else:
            print(f" Test {i}:{ERROR_COLOR} Failed {END_COLOR}")
        i += 1

    return 1 if score == len(test_data) else 0


# test case for function remove_duplicate
def test_remove_duplicate(fn):
    test_data = {(3,8,9,3,1): 4,
                 (3,8,9,3,1,2,8,3): 5,
                 (3,8,9,1): 4,
                 (1,5,"t","z","t",1,8): 5,
                 ('a','z',2,'a','e','c','c','a'): 5,
                 ('apple','ball','cat','oranges','cat'): 4
                 }
    i = 0
    score = 0
    for tuple_in, result in test_data.items():
        returned_tuple = fn(tuple_in) or ()
        if result == len(returned_tuple):
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
