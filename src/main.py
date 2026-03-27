import pandas as pd
import numpy as np


def problem1():
    my_set: set[str] = {"a", "b", "c", "d"}
    # ERROR because a set doesn't have a defined ordering
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
    # (1 points)  Create a DF1 data frame using S1, S2, S3 and S4

    S1 = pd.Series(["a", "b", "c", "d"], index=[10, 20, 30, 40])

    S2 = pd.Series(["e", "f", "g", "h"], index=[10, 20, 30, 40])

    S3 = pd.Series(["i", "j", "k", "l"], index=[10, 20, 30, 40])

    S4 = pd.Series(["m", "n", "o", "p"], index=[10, 20, 30, 40])

    DF1 = pd.concat([S1, S2, S3, S4], axis=1)
    print(DF1)

    # (18 points)Create data frames That have as values the same values as DF1 (with the same structure) but instead of first creating series S1,S2,S3 and S4 do the following
    # Create DF2 from set of sets

    bak_DF2 = {
        frozenset(["a", "b", "c", "d"]),
        frozenset(["e", "f", "g", "h"]),
        frozenset(["i", "j", "k", "l"]),
        frozenset(["m", "n", "o", "p"]),
    }
    # Doesnt work as expected as sets are unordered
    # DF2
    #     0  1  2  3
    # 10  o  g  c  l
    # 20  m  h  d  j
    # 30  p  f  a  i
    # 40  n  e  b  k

    _DF2 = [
        ["a", "b", "c", "d"],
        ["e", "f", "g", "h"],
        ["i", "j", "k", "l"],
        ["m", "n", "o", "p"],
    ]

    DF2 = pd.DataFrame(_DF2).T
    DF2.index = [10, 20, 30, 40]
    print("DF2")
    print(DF2)

    # Create DF3 from list of lists

    _DF3 = [
        ["a", "b", "c", "d"],
        ["e", "f", "g", "h"],
        ["i", "j", "k", "l"],
        ["m", "n", "o", "p"],
    ]

    DF3 = pd.DataFrame(_DF3).T
    DF3.index = [10, 20, 30, 40]
    print("DF3")
    print(DF3)

    # Create DF4 from array of arrays
    _DF4 = np.array(
        [
            np.array(["a", "b", "c", "d"]),
            np.array(["e", "f", "g", "h"]),
            np.array(["i", "j", "k", "l"]),
            np.array(["m", "n", "o", "p"]),
        ]
    )

    DF4 = pd.DataFrame(_DF4).T
    DF4.index = [10, 20, 30, 40]
    print("DF4")
    print(DF4)

    # Create DF5 from dictionary of dictionaries
    _DF5 = {
        0: {10: "a", 20: "b", 30: "c", 40: "d"},
        1: {10: "e", 20: "f", 30: "g", 40: "h"},
        2: {10: "i", 20: "j", 30: "k", 40: "l"},
        3: {10: "m", 20: "n", 30: "o", 40: "p"},
    }
    DF5 = pd.DataFrame(_DF5)
    print("DF5")
    print(DF5)

    # Create DF6 from lists of dictionaries

    _DF6 = [
        {10: "a", 20: "b", 30: "c", 40: "d"},
        {10: "e", 20: "f", 30: "g", 40: "h"},
        {10: "i", 20: "j", 30: "k", 40: "l"},
        {10: "m", 20: "n", 30: "o", 40: "p"},
    ]
    DF6 = pd.DataFrame(_DF6).T
    print("DF6")
    print(DF6)

    # Create DF7 from dictionary of lists
    _DF7 = {
        0: ["a", "b", "c", "d"],
        1: ["e", "f", "g", "h"],
        2: ["i", "j", "k", "l"],
        3: ["m", "n", "o", "p"],
    }

    DF7 = pd.DataFrame(_DF7)
    DF7.index = [10, 20, 30, 40]
    print("DF7")
    print(DF7)


def problem5():
    S1 = pd.Series(["a", "b", "c", "d"], index=[10, 20, 30, 40])

    S2 = pd.Series(["e", "f", "g", "h"], index=[10, 20, 30, 40])

    S3 = pd.Series(["i", "j", "k", "l"], index=[10, 20, 30, 40])

    S4 = pd.Series(["m", "n", "o", "p"], index=[10, 20, 30, 40])

    DF1 = pd.concat([S1, S2, S3, S4], axis=1)
    print(DF1)

    # (18 points)Create data frames That have as values the same values as DF1 (with the same structure) but instead of first creating series S1,S2,S3 and S4 do the following
    # Create DF2 from set of sets

    bak_DF2 = {
        frozenset(["a", "b", "c", "d"]),
        frozenset(["e", "f", "g", "h"]),
        frozenset(["i", "j", "k", "l"]),
        frozenset(["m", "n", "o", "p"]),
    }
    # Doesnt work as expected as sets are unordered
    # DF2
    #     0  1  2  3
    # 10  o  g  c  l
    # 20  m  h  d  j
    # 30  p  f  a  i
    # 40  n  e  b  k

    _DF2 = [
        ["a", "b", "c", "d"],
        ["e", "f", "g", "h"],
        ["i", "j", "k", "l"],
        ["m", "n", "o", "p"],
    ]

    DF2 = pd.DataFrame(_DF2).T
    DF2.index = [10, 20, 30, 40]
    print("DF2")
    print(DF2)
    # (2 points) Concatenate DF1 and DF2 so that you end up having 8 rows
    DF1_2 = pd.concat([DF1, DF2])
    print(DF1_2)

    # (2 points) Insert as first column S0 with values 1,2,2,3,3,4,4,5
    DF1_2.insert(0, "S0", np.array([1, 2, 2, 3, 3, 4, 4, 5]))
    print(DF1_2)

    # (2 points) Use hierarchical indexing so that S0 is used as the second level index
    DF1_2 = DF1_2.set_index("S0", append=True)

    # (3 points) Group by the index and concatenate the values
    grouped1 = DF1_2.groupby(level=0).aggregate(lambda col: "".join(col.astype(str)))
    print(grouped1)

    # (3 points) Group by first column S0 and concatenate the values
    grouped2 = DF1_2.groupby("S0").aggregate(lambda col: "".join(col.astype(str)))
    print(grouped2)


def main():
    print("== PROBLEM 1 ==")
    problem1()
    print("== PROBLEM 2 ==")
    problem2()
    print("== PROBLEM 3 ==")
    problem3()
    print("== PROBLEM 4 ==")
    problem4()
    print("== PROBLEM 5 ==")
    problem5()


if __name__ == "__main__":
    main()
