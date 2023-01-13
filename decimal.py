#!/usr/bin/env python3
# Created by: Joanne Santhosh
# Created on: Jan 2023
# This program passes by reference

from typing import List


def round_off_number(decimal: List[float], decimal_places: int) -> None:
    # This function rounds off decimal numbers

    rounded_decimal = decimal[0] * (10**decimal_places)
    rounded_decimal = rounded_decimal + 0.5
    rounded_decimal = int(rounded_decimal)
    rounded_decimal = rounded_decimal / (10**decimal_places)

    decimal[0] = rounded_decimal


def main():
    # this function gets a decimal and rounds off the decimal

    decimal_number = []

    # input
    user_number = input("Enter the number you want to round: ")
    decimal_places = input("Enter how many decimal places do you want to round by: ")

    try:
        user_number = float(user_number)
        decimal_places = int(decimal_places)

        decimal_number.append(user_number)

        # calls function
        round_off_number(decimal_number, decimal_places)

        print("\nThe rounded number is {0}".format(decimal_number[0]))

    except Exception:
        print("\nInvalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
