# Project: days to hours calculator
# Purpose: conversion of time in the unit of hours. Calculations will be from days and converted into hours


calculations_to_hours = 24  # calculations for days hours
name_of_unit = "hours"


# user should not enter 0
def days_to_units(num_of_days):
    conditional_check = num_of_days > 0
    print(type(conditional_check))

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculations_to_hours} {name_of_unit}"
    elif num_of_days == 0:
        return "you entered a 0, please enter a valid positive number"


# user should not enter a negative number
def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")

    except ValueError:
        print("your input is not a number. Don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
    for num_of_days_element in user_input.split(","):
        validate_and_execute()


print("Thank You for using my program")
