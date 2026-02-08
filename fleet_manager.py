# note i havent actually watched star trek so i dont have a clue if these characters and their divisions are factual

n = ["Airiam", "Jonathan Archer", "Ascencia", "Soji Asha", "Ayala"]
r = ["Lt, Commander", "Captain", "Civilian", "Civilian", "Lieutenant"]
d = ["Command", "Operations", "None", "None", "Security"]
id = ["5423","9867", "9068", "1654", "3459"]


def display_roster():
    print("NAME -- RANK -- ID")
    for i in range(len(n)):
        print(f"{n[i]} -- {r[i]} -- {id[i]}")
    
    display_menu()


def add_member():
    new_n = str(input("enter name to add: ")).title().strip()
    new_r = str(input("enter rank: ")).title().strip()
    new_d = str(input("enter division: ")).title().strip()
    new_id = str(input("enter ID: ")).strip()

    n.append(new_n)
    r.append(new_r)
    d.append(new_d)
    id.append(new_id)
    
    print("New member added.")
    display_menu()


# function to remove the members from the system
def remove_member():
    #prompt the user to enter the name they would like to remove 
    name = str(input("who would like to remove: ")).title().strip()
    
    # while loop to make sure a valid name is entered
    while name not in n:
        print("name is not in list.")
        name = str(input("who would like to remove: ")).title().strip()
    else:
       # pops the data from their respective lists
       idx = n.index(name)
       n.pop(idx)
       r.pop(idx)
       d.pop(idx)
       id.pop(idx)

    print("Member removed.")

    display_menu()


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

    userinput = int(input("Enter option: "))
    
    #if statements to determine what the outcome is
    if userinput == 1:
        display_roster()
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
        exit

#asks the user for their full name as their login and prints it our when done
login = str(input("Enter full name: \n")).title().strip()
print(f"Welcome {login}.")

display_menu()