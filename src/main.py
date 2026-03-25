import pandas as pd
import numpy as np


def problem1():
    my_set: set[str] = {"a", "b", "c", "d"}
    # NOTE: because a set doesn't have a defined ordering
    # we have to convert it into a list first, before constructing the Series
    s1 = pd.Series(list(my_set))
    print("== SET ==")
    print(s1)

    l: list = ["a", "b", "c", "d"]
    s2 = pd.Series(l)
    print("== LIST ==")
    print(s2)

    print("== ARRAY ==")
    arr = np.array(["a", "b", "c", "d"])
    s3 = pd.Series(arr)
    print(s3)

    # Use keys that follow the automatic indices given by constructor
    d: dict = {0: "a", 1: "b", 2: "c", 3: "d"}
    s4 = pd.Series(d)
    print("== DICTIONARY ==")
    print(s4)


def problem2():
    index = pd.Index([10, 20, 30, 40])
    my_set: set[str] = {"a", "b", "c", "d"}
    # NOTE: because a set doesn't have a defined ordering
    # we have to convert it into a list first, before constructing the Series
    s1 = pd.Series(list(my_set), index=index)
    print("== SET ==")
    print(s1)

    l: list = ["a", "b", "c", "d"]
    s2 = pd.Series(l, index=index)
    print("== LIST ==")
    print(s2)

    print("== ARRAY ==")
    arr = np.array(["a", "b", "c", "d"])
    s3 = pd.Series(arr, index=index)
    print(s3)

    d: dict = {10: "a", 20: "b", 30: "c", 40: "d"}
    s4 = pd.Series(d)
    print("== DICTIONARY ==")
    print(s4)


def problem3():
    index = pd.Index([10, 20, 30, 40])
    my_set: set[str] = {"a", "b", "c", "d"}
    # python sets dont enforce order, so we have to convert and sort the set
    s1 = pd.Series(sorted(list(my_set)), index=index)
    print(s1)

    # use list instead
    s2 = pd.Series(["e", "f", "g", "h"], index=index)
    print(s2)

    # use array instead
    s3 = pd.Series(np.array(["i", "j", "k", "l"]), index=index)
    print(s3)

    # use set again
    my_set: set[str] = {"m", "n", "o", "p"}
    s4 = pd.Series(sorted(list(my_set)), index=index)
    print(s4)


def problem4():
    pass


def main():
    problem1()
    problem2()
    problem3()


if __name__ == "__main__":
    main()
