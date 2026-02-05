# note i havent actually watched star trek so i dont have a clue if these characters and their divisions are factual

n = ["Airiam", "Jonathan Archer", "Ascencia", "Soji Asha", "Ayala"]
r = ["Lt, Commander", "Captain", "Civilian", "Civilian", "Lieutenant"]
d = ["Command", "Operations", "None", "None", "Security"]
id = ["5423","9867", "9068", "1654", "3459"]




# created the display_menu function
def display_menu():

    print("===Menu===")
    print("1 - View members")
    print("2 - add members")
    print("3 - remove member")
    print("4 - Update rank")
    print("5 - Search crew")
    print("6 - Filter By Division")
    print("7 - Calculate Payroll")
    print("8 - Count Officers")
    print("9 - Exit")


    while userinput > 0 and userinput < 5:
        # asks the user for their input choice
        userinput = int(input("Enter option: \n"))
    
        #if statements to determine what the outcome is
        if userinput == 1:
            init_database()
        elif userinput == 2:
            add_member()
        elif userinput == 3:
            remove_member()
        elif userinput == 4:
            update_rank()
        elif userinput == 5:
            search_crew()
        elif userinput == 6:
            filter_by_div()
        elif userinput == 7:
            calculate_payroll()
        elif userinput == 8:
            count_officers()
        else:
            break

#asks the user for their full name as their login and prints it our when done
login = str(input("Enter full name: \n")).title().strip()
print(f"Welcome {login}.")

display_menu()