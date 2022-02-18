colculation_to_units = 24
name_of_units = "hours"

def days_to_units(number_of_days):
        
    return(f"{number_of_days} days are {number_of_days*colculation_to_units} {name_of_units}")

def validate_and_execute():
    
    try:
        user_input_number = int(number_of_days_element)
        # only posetive integesr
        if user_input_number>0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered zero, please enter a valid positive number")
        else:
            print("you entered negative, please enter a valid positive number")
    except ValueError:
        print("your input is not a number. Don't ruin my program!")

user_input = ""
while user_input != "exit":
    user_input = input("Type value\n")
    list_of_days= user_input.split(",")
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))
    print(user_input.split(","))
    for number_of_days_element in set(user_input.split(",")):
        validate_and_execute()