#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: jan 2023
# This program uses a function by reference


def add_one(someVariable):
    # function adds 1, by reference

    someVariable[0] = someVariable[0] + 1

def main():
    # this function gets a number and calls the add_one function

    someNumber = []
    # input
    temp_var = int(input("Enter a number: "))
    someNumber.append(temp_var)
    add_one(someNumber)
    print(someNumber[0])

if __name__ == "__main__":
    main()
